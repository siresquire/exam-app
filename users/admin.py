from django.contrib import admin
from .models import Student
from .models import Lecturer
from .models import Attendant
from .models import Faculty
from .models import Department
from .models import Program
from .models import Course
from .models import Exam
from .models import Exam_Room
from .models import Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Attendant)
admin.site.register(Lecturer)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Exam_Room)
admin.site.register(Attendance)