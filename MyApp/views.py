
# these are the rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# these are django imports
from django.db.models import Sum ,Avg

# these are local imports
from .models import Student ,Teacher
from .serializers import StudentSerializers ,TeacherSerializers
from .utils import calculate_passing_percentage


# Create your views here.

'''
This is the StudentView class which is used to handle the CRUD operations on the Student model.
'''
class StudentView(APIView):

    '''
    this method is used to get the student data based on the rollno and retrieve all the students data

    Accepts:
        - rollno (optional):int datatype
    Returns:
        - 200 OK: List of students or student data in JSON format
        - 404 NOT FOUND: Error message if student data is not found


    '''
    
    def get(self, request, rollno=None):
    
        if rollno is not None:
            try:
                student = Student.objects.get(rollno=rollno)
                serializer = StudentSerializers(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error": "Student Data not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializers(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    '''
    this method is used to craete and add new student to the database

    Accepts:
        - request.data: JSON object containing student information
    Returns:
        - 201 CREATED: Created student data in JSON format
        - 400 BAD REQUEST: Error message if validation fails

    '''
    
    def post(self, request):
        serialize=StudentSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    '''
    this method is used to update the student data based on the rollno

     Accepts:
        - rollno: int datatype
        - request.data: JSON object containing updated student information (The JSON object should contain all manditary fields
        like :
            name, 
            teacher_id,
            maths_marks,
            physics_marks,
            chemistry_marks,
            )
    Returns:
        - 202 ACCEPTED: Updated student data in JSON format
        - 404 NOT FOUND: Error message if student data is not found
        - 400 BAD REQUEST: Error message if validation fails
    '''
  
        
    def put(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

    ''' 
    this method is used to update the student data partially based on the rollno

    Accepts:
        - rollno:  int datatype
        - request.data: JSON object containing fields to update (partial data) ie., which / which are the fields need to updated
        like :
            name,
            teacher_id,
            maths_marks,
            physics_marks,
            chemistry_marks,
            )
    Returns:
        - 202 ACCEPTED: Updated student data in JSON format
        - 404 NOT FOUND: Error message if student data is not found
        - 400 BAD REQUEST: Error message if validation fails

    '''
    

    def patch(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    '''
    this method is used to delete the student data based on the rollno

    Accepts:
        - rollno: int dtatype
    Returns:
        - 204 NO CONTENT: Success message indicating data deletion
        - 404 NOT FOUND: Error message if student data is not found

    '''
    
    
    def delete(self, request, rollno):
        try:
            student=Student.objects.get(rollno=rollno)
        except Student.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Roll NUmber is not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"Sucess": "Data Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    


'''
This is the TopperView class which is used to get the topper of the class based on the total marks
Accepts:
    - request: API request
Returns:
    - 200 OK: List of top 5 students in JSON format

'''
    
class TopperView(APIView):
    def get(self, request):
        topper=Student.objects.order_by('-total_marks')[:5]
        serializer=StudentSerializers(topper,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

'''
This is the HaveCut_off class which is used to get the students who have the cutoff or not
Accepts:
    - request: API Request 
    - cutoff: str (either "cutoff" or "nocutoff")
Returns:
    - 200 OK: List of students meeting the cutoff criteria in JSON format
'''
    
class HaveCut_off(APIView):
    def get(self, request,cutoff):
        if cutoff=="cutoff":
            topper=Student.objects.filter(total_marks__gte=calculate_passing_percentage())
            serializer=StudentSerializers(topper, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif cutoff=="nocutoff":
            topper=Student.objects.filter(total_marks__lte=calculate_passing_percentage())
            serializer=StudentSerializers(topper, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
'''
This is the PassOrNot class which is used to get the students who have passed or not based on the spass parameter,
where spass can be pass or notpass

Accepts:
    - request: API Request 
    - spass: str (either "pass" or "notpass")
    - rollno (optional): int 
Returns:
    - 200 OK: List of students or specific student data in JSON format
'''
    
class PassOrNot(APIView):
    def get(self, request,spass, rollno=None):
        
        if rollno is not None:
            student=Student.objects.get(rollno=rollno)
            serializer=StudentSerializers(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        if spass=="pass":
            student=Student.objects.filter(result=True)
            serializer=StudentSerializers(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif spass=="notpass":
            student=Student.objects.filter(result=False)
            serializer=StudentSerializers(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
'''
This is the HaveAvg class which is used to get the students who have the average marks or not based on the avg parameter,
where avg can be avg or noavg

Accepts:
    - request: API Request 
    - avg: str (either "avg" or "noavg")
    - rollno (optional): int 
Returns:
    - 200 OK: List of students or specific student data in JSON format

'''

class HaveAvg(APIView):
    def get(self,requset, avg,rollno=None):
        total_avg_marks = Student.objects.aggregate(total=Avg('total_marks'))['total'] 
        

        if rollno is not None:
            student=Student.objects.get(rollno=rollno)
            serializer=StudentSerializers(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if avg=="avg":
            student=Student.objects.filter(total_marks__gte=total_avg_marks)
            serializer=StudentSerializers(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif avg=="noavg":
            student=Student.objects.filter(total_marks__lte=total_avg_marks)
            serializer=StudentSerializers(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
'''
This method retrieves performance for each teacher based on student results.
Accepts:
    - request: API Request
Returns:
    - 200 OK: Performance data of teachers and best teachers in JSON format
'''


class TeacherPerformance(APIView):
    def get(self, request):
        # Get distinct teacher IDs
        teachers = Teacher.objects.all()
        teacher_performance = []
        best_teachers = []
        high_pass = 0
        highpassing_percentage = 0

        for teacher in teachers:
            # Fetch students for the current teacher
            student_teacher = Student.objects.filter(teacher_id=teacher)
            total_students = student_teacher.count()
            passed_students = student_teacher.filter(result=True).count()
            avg_marks = student_teacher.aggregate(avg_marks=Avg('total_marks'))['avg_marks'] or 0


            passing_percentage = 0
            if total_students > 0:
                passing_percentage = (passed_students / total_students * 100)


            # Append performance data for the teacher
            teacher_performance.append({
                'teacher_id': teacher.empid,  # Assuming empid is the identifier
                'teacher_name': teacher.name,
                'total_students': total_students,
                'passed_students': passed_students,
                'avg_marks': avg_marks,
                'passing_percentage': passing_percentage,
            })

            # Check if this teacher has the highest number of passed students
            if passing_percentage  > highpassing_percentage :
                highpassing_percentage = passing_percentage
                best_teachers = [teacher.name]  # Store teacher names as strings
            elif passing_percentage == highpassing_percentage:
                best_teachers.append(teacher.name)  # Add teacher name to the list

        response_data = {
            'performance': teacher_performance,
            'best_teachers': best_teachers,
            'Passing_Percent': highpassing_percentage
        }

        return Response(response_data, status=status.HTTP_200_OK)

'''
This is the TeacherView class which is used to handle the CRUD operations on the Teacher model.

'''


class TeacherView(APIView):

    '''
    this method is used to get the teacher data based on the empid and retrieve all the teachers data

    Accepts:
        - request: API Request 
        - empid (optional): int 
    Returns:
        - 200 OK: Teacher data or list of teachers in JSON format
        - 404 NOT FOUND: Error message if teacher data is not found

    '''
    def get(self, request, empid=None):
        if empid is not None:
            try:
                teacher = Teacher.objects.get(empid=empid)
                serializer = TeacherSerializers(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response({"error": "Teacher Data not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializers(teachers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    '''
    this method is used to craete and add new teacher to the database
    Accepts:
        - request: API Request containing teacher data in JSON format with all the required field ie., empid and name
    Returns:
        - 201 CREATED: Created teacher data in JSON format
        - 400 BAD REQUEST: Error message if validation fails

    '''

    def post(self, request):
        serialize = TeacherSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    

    '''
    this method is used to update the teacher data based on the empid
     Accepts:
        - request: API Request containing updated teacher data in JSON format with all mandatory fields 
        - empid:int
    Returns:
        - 202 ACCEPTED: Updated teacher data in JSON format
        - 404 NOT FOUND: Error message if teacher data is not found
        - 400 BAD REQUEST: Error message if validation fails
    '''

    def put(self, request, empid):
        try:
            teacher = Teacher.objects.get(empid=empid)
        except Teacher.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Empid is not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


    '''
    this method is used to update the teacher data partially based on the empid

    Accepts:
        - request: API Request containing partial teacher data in JSON format
        - empid: int
    Returns:
        - 202 ACCEPTED: Updated teacher data in JSON format
        - 404 NOT FOUND: Error message if teacher data is not found
        - 400 BAD REQUEST: Error message if validation fails
    '''


    def patch(self, request, empid):
        try:
            teacher = Teacher.objects.get(empid=empid)
        except Teacher.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Empid is not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializers(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

    '''
    this method is used to delete the teacher data based on the empid
    Accepts:
        - request: API Request object
        - empid: int
    Returns:
        - 204 NO CONTENT: Success message indicating data deletion
        - 404 NOT FOUND: Error message if teacher data is not found
    '''

    def delete(self, request, empid):
        try:
            teacher = Teacher.objects.get(empid=empid)
        except Teacher.DoesNotExist:
            return Response({"Message": "Sorry Given Provided Empid is not exist"}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({"Sucess": "Data Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)