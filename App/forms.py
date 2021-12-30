# import form class from django
from django import forms
from .models import createResume

# create a ModelForm
class Resumedata(forms.ModelForm):
	class Meta:
		model = createResume
		fields = ['name','address','phone','email','aboutyou','careerobj','ssc','hsc','college','degree','cgpa','j3sd','j3ed','positiondet3','j2sd','j2ed','positiondet2','j1sd','j1ed','positiondet1','references']
