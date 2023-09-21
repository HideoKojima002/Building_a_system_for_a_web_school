from rest_framework import serializers
from .models import *


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonWatch
        fields = '__all__'


class LessonWithAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    status = serializers.SerializerMethodField()
    watch_time_seconds = serializers.SerializerMethodField()

    def get_status(self, obj):
        user = self.context['request'].user
        try:
            lesson_watch = LessonWatch.objects.get(user=user, lesson=obj)
            return "Просмотрено" if lesson_watch.watched else "Не просмотрено"
        except LessonWatch.DoesNotExist:
            return "Не просмотрено"

    def get_watch_time_seconds(self, obj):
        user = self.context['request'].user
        try:
            lesson_watch = LessonWatch.objects.get(user=user, lesson=obj)
            return lesson_watch.watch_time_seconds
        except LessonWatch.DoesNotExist:
            return 0


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    status = serializers.SerializerMethodField()
    watch_time_seconds = serializers.SerializerMethodField()
    last_watched_date = serializers.SerializerMethodField()

    def get_status(self, obj):
        user = self.context['request'].user
        try:
            lesson_watch = LessonWatch.objects.get(user=user, lesson=obj)
            return "Просмотрено" if lesson_watch.watched else "Не просмотрено"
        except LessonWatch.DoesNotExist:
            return "Не просмотрено"

    def get_watch_time_seconds(self, obj):
        user = self.context['request'].user
        try:
            lesson_watch = LessonWatch.objects.get(user=user, lesson=obj)
            return lesson_watch.watch_time_seconds
        except LessonWatch.DoesNotExist:
            return 0

    def get_last_watched_date(self, obj):
        user = self.context['request'].user
        try:
            lesson_watch = LessonWatch.objects.get(user=user, lesson=obj)
            return lesson_watch.last_watched_date
        except LessonWatch.DoesNotExist:
            return None


class ProductStatisticsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(source='id')
    product_name = serializers.CharField(source='name')
    lessons_viewed = serializers.IntegerField()
    total_watch_time_seconds = serializers.IntegerField()
    total_students= serializers.IntegerField()
    acquisition_percentage =serializers.DecimalField(max_digits=5, decimal_places=2)

