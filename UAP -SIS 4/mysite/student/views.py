def exam_routine(request):
    routines = ExamRoutine.objects.all()
    form = ExamRoutineForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student:exam_routine')

    context = {
        'form': form,
        'routines': routines
    }
    return render(request, 'student/exam_routine.html', context)


def add_exam_routine(request):
    form = ExamRoutineForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student:exam_routine')

    return render(request, 'student/add_exam_routine.html', {'form': form})


def delete_exam_routine(request, pk):
    routine = get_object_or_404(ExamRoutine, pk=pk)

    if request.method == "POST":
        routine.delete()

    return redirect('student:exam_routine')
