class ExamRoutineForm(forms.ModelForm):
    class Meta:
        model = ExamRoutine
        fields = ['title', 'pdf_file']
