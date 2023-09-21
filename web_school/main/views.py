from django.shortcuts import render
from django.db.models import Case, When, BooleanField
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Access, Product, Lesson
from .serializers import *


# def context_func():
#     lessons = Lesson.objects.all()
#     access = Access.objects.all()
#     products = Product.objects.all()
#     context = {
#         'lessons': lessons,
#         'access': access,
#         'product': products,
#     }
#
#     return context


def index(request):
    return render(request, 'main/index.html')


class LessonListWithAccessAPIView(generics.ListAPIView):
    serializer_class = LessonWithAccessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        accessible_lessons = Lesson.objects.filter(products__owner=user)
        return accessible_lessons

        # user = self.request.user
        # product_id = self.kwargs.get('product_id')

        # lessons = Lesson.objects.filter(products__id=product_id)
        #
        # #
        # lessons = lessons.annotate(
        #     watched=Case(
        #         When(lessonwatch__user=user, lessonwatch__watched=True, then=True),
        #         default=False,
        #         output_field=BooleanField()
        #     )
        # )
        #
        # return lessons


class AccessListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AccessSerializer

    def get_queryset(self):
        user = self.request.user
        return Access.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        product_id = request.data.get('product')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)

        if product.owner == user:
            return Response({'message': 'Вы не можете предоставить доступ к своему собственному продукту'}, status=status.HTTP_400_BAD_REQUEST)

        access, created = Access.objects.get_or_create(user=user, product=product)
        if created:
            return Response({'message': 'Доступ предоставлен успешно.'})
        else:
            return Response({'message': 'Вы уже имеете доступ к этому продукту.'})


class AccessDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = AccessSerializer

    def get_queryset(self):
        user = self.request.user
        return Access.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Доступ удален успешно.'})


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonWatchListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonWatchSerializer

    def get_queryset(self):
        user = self.request.user
        return LessonWatch.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        lesson_id = request.data.get('lesson')
        try:
            lesson = Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return Response({'message': 'Урок не найден'}, status=status.HTTP_404_NOT_FOUND)

        lesson_watch, created = LessonWatch.objects.get_or_create(user=user, lesson=lesson)
        if created:
            return Response({'message': 'Информация о просмотре урока создана успешно.'})
        else:
            return Response({'message': 'Информация о просмотре урока уже существует.'})


class LessonWatchDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = LessonWatch.objects.all()
    serializer_class = LessonWatchSerializer


class AccessRequestCreateAPIView(generics.CreateAPIView):
    serializer_class = AccessSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AccessListManageAPIView(generics.ListCreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [IsAdminUser]


class LessonListForProductAPIView(generics.ListAPIView):
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')  # По логике тут мы получаем ID продукта из URL

        accessible_lessons = Lesson.objects.filter(products__owner=user, products__id=product_id)
        return accessible_lessons


class ProductStatisticsAPIView(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        products = Product.objects.all()
        statistics = []

        for product in products:
            lessons = LessonWatch.objects.filter(lesson__products=product, watched=True)
            total_users_on_platform = User.objects.count()
            total_watch_time_seconds = lessons.aggregate(total_watch_time_seconds=models.Sum('watch_time_seconds'))['total_watch_time_seconds'] or 0
            students = Access.objects.filter(product=product).count()
            acquisition_percentage = (students / total_users_on_platform) * 100  # ТАк я определил процент приобретенных продуктов

            statistics.append({
                'id': product.id,
                'name': product.name,
                'lessons_viewed': lessons.count(),
                'total_watch_time_seconds': total_watch_time_seconds,
                'total_students': students,
                'acquisition_percentage': round(acquisition_percentage, 2),
            })

        return statistics
