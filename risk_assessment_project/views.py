from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import RiskAssessment, UserAssessment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  # Import the get_user_model function
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
import pandas as pd
from django.http import JsonResponse


def signup(request):
    User = get_user_model()  # Get the custom user model or the default User model

    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user=form.save()

            
            return redirect('login')  # Redirect to login page after successful signup
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_logout(request):
    if request.user.is_authenticated and request.method == 'GET':
        logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    redirect_authenticated_user = True  # Redirect if user is already authenticated

    def get_success_url(self):
        return reverse_lazy('risk_assessment_page')  # Replace 'risk_assessment_page' with your home page URL name
    
@login_required
def risk_assessment_page(request):
    assessments = RiskAssessment.objects.filter(status=True).all()
    
    return render(request, 'risk_assessment_page.html', {'assessments': assessments})

@login_required
def get_user_assessment_assement_id(request, user_assessment_id):
    try:
        user_assessment = UserAssessment.objects.get(id=user_assessment_id, user=request.user)
        data = {
            'likelihood': user_assessment.likelihood,
            'impact': user_assessment.impact,
            'exposure': user_assessment.exposure,
            'risk_level': user_assessment.risk_level
        }
        czc
        return JsonResponse(data)
    
    except UserAssessment.DoesNotExist:
        return JsonResponse({'error': 'User Assessment not found'}, status=404)

@login_required
def get_user_assessments(request, risk_assessment_id):
    user_assessments = UserAssessment.objects.filter(risk_assessment_id=risk_assessment_id,user=request.user).values('likelihood', 'impact', 'exposure', 'risk_level')
    return JsonResponse(list(user_assessments), safe=False)

def import_from_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        # Check if the uploaded file is an Excel file
        if excel_file.name.endswith('.xlsx'):
            # Read the Excel file using pandas
            df = pd.read_excel(excel_file)

            # Iterate through rows and save data to RiskAssessment model
            for _, row in df.iterrows():
                RiskAssessment.objects.create(
                    main_control=row['الضابط الأساسي (main control)'],
                    subcontrol=row['الضابط الفرعي (sub control)'],
                    control_details=row['تفاصيل الضابط        ( control details)']
                    # Add other fields as needed
                )
            sdf
            return redirect('risk_assessment_page')  # Redirect after successful import

    # Handle GET requests or invalid file uploads
    return redirect('risk_assessment_page')

@login_required
def add_assessment(request):
    if request.method == 'POST':
        # Get the risk_assessment ID from the form
        risk_assessment_id = request.POST.get('risk_assessment_id')
       

        # Get the RiskAssessment object using the risk_assessment_id
        risk_assessment = RiskAssessment.objects.get(id=risk_assessment_id)

        # Create UserAssessment for the obtained RiskAssessment
        likelihood = request.POST.get('likelihood', '')
        impact = request.POST.get('impact', '')
        exposure = request.POST.get('exposure', '')
        risk_level = request.POST.get('risk_level', '')

        UserAssessment.objects.create(
            risk_assessment=risk_assessment,
            likelihood=likelihood,
            impact=impact,
            exposure=exposure,
            risk_level=risk_level,
            user=request.user
        )
        fds
        return redirect('risk_assessment_page')

    return render(request, 'add_assessment.html')

@login_required
def delete_user_assessment(request):
    # Get the UserAssessment instance or return a 404 error if not found
    user_assessment = get_object_or_404(UserAssessment, user=request.user)

    # Check if the UserAssessment belongs to the current user
    if user_assessment.user == request.user:
        # Delete the UserAssessment instance
        user_assessment.delete()
        ada
        return redirect('risk_assessment_page')  # Redirect to a suitable URL
    
@login_required
def change_status(request, assessment_id):
    assessment = get_object_or_404(RiskAssessment, id=assessment_id)
    assessment.status = False
    assessment.save()
    dadas
    return redirect('risk_assessment_page')

@login_required
def add_user_control(request):
    if request.method == 'POST':
        main_control = request.POST.get('main_control')
        subcontrol = request.POST.get('subcontrol')
        control_details = request.POST.get('control_details')
        ssd
        # Create a new RiskAssessment instance
        RiskAssessment.objects.create(
            user=request.user,
            main_control=main_control,
            subcontrol=subcontrol,
            control_details=control_details
        )

        # Optionally, you can return a JSON response indicating success
        return redirect('risk_assessment_page')
    else:
        # Handle GET requests if needed
        return render(request, 'your_template.html')