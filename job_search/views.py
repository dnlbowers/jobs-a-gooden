from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Job, PinnedJobs, Notes
from .forms import NoteForm, AddJobForm
from django.contrib.messages.views import SuccessMessageMixin


# ~ADD DOCSTRINGS
class AddJob(generic.CreateView):
    form_class = AddJobForm
    template_name = 'job_search/pages/add-job.html'
    success_url = reverse_lazy('add_job')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(AddJob, self).form_valid(form)
        return redirect('add_job')


class JobList(generic.ListView):
    model = Job
    paginate_by = 6
    template_name = 'job_search/pages/job-list.html'
    context_object_name = 'jobs'
    queryset = Job.objects.filter(status=1).order_by('-date_posted')


class FullJobSpec(View):
    def get(self, request, id, *args, **kwargs):
        queryset = Job.objects.filter(status=1)
        job_spec = get_object_or_404(queryset, id=id)
        # get all notes by user
        notes = job_spec.related_job.all().order_by('-date_created')
        author = self.request.user.id
        pinned = False
        if job_spec.is_pinned.filter(id=self.request.user.id).exists():
            pinned = True

        return render(
            request,
            'job_search/pages/job-details.html',
            {
                'author': author,
                "job": job_spec,
                "pinned": pinned,
                'notes': notes,
                'note_made': False,  # boolean to to use as conditional
                'note_form': NoteForm()
            },
        )

    def post(self, request, id, *args, **kwargs):
        queryset = Job.objects.filter(status=1)
        job_spec = get_object_or_404(queryset, id=id)
        notes = job_spec.related_job.all().order_by('-date_created')
        author = self.request.user.id
        pinned = False
        if job_spec.is_pinned.filter(id=self.request.user.id).exists():
            pinned = True

        note_form = NoteForm(data=request.POST)

        if note_form.is_valid():
            note = Notes()
            note.short_description = note_form.cleaned_data[
                'short_description'
                ]
            note.note = note_form.cleaned_data['note']
            note.is_insight = note_form.cleaned_data['is_insight']
            note.related_job = Job.objects.get(id=id)
            note.user = request.user
            note.save()
            return HttpResponseRedirect(reverse('note_made', args=[id]))

        else:
            note_form = NoteForm()

        return render(
            request,
            'job_search/pages/job-details.html',
            {
                'author': author,
                "job": job_spec,
                "pinned": pinned,
                'notes': notes,
                'note_made': True,  # boolean to to use as conditional
                'note_form': NoteForm()
            },
        )


class PinJob(View):
    def post(self, request, id):
        # get the status of the toggle from post request in JS file
        status = True if request.POST['status'] == 'true' else False
        # Identify the job being toggled
        job = Job.objects.get(id=id)
        # identify the users pinned job database table
        pinned = PinnedJobs.objects.get(user=request.user)

        if status:
            # add to manytomany list
            pinned.pinned_jobs.add(job)
            # add user to is_pinned
            job.is_pinned.add(request.user)
        else:
            # remove from manytomany list
            pinned.pinned_jobs.remove(job)
            # remove user from is_pinned
            job.is_pinned.remove(request.user)

        return HttpResponse(200)


class PinnedPosts(generic.ListView):
    model = PinnedJobs
    paginate_by = 6
    template_name = 'job_search/pages/pinboard.html'
    context_object_name = 'jobs'
    # queryset = Job.objects.filter(status=1).order_by('-date_posted')

    def get_queryset(self):
        # get all pinned posts by user
        pinned = PinnedJobs.objects.get(user=self.request.user)
        # get all jobs from the many to many list
        jobs = pinned.pinned_jobs.all()
        return jobs


class DisplayInsights(generic.ListView):
    model = Notes
    paginate_by = 6
    template_name = 'job_search/pages/insights.html'
    context_object_name = 'insights'
    queryset = Notes.objects.filter(is_insight=True).order_by('-date_created')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class DeleteNote(View):
    # delete note from database (check why the params work like they do)
    @staticmethod
    def post(request, id):
        delete_note = Notes.objects.get(id=id)
        delete_note.delete()
        return HttpResponse(200)


class DeleteJob(View):
    # delete job from database (check why the params work like they do)
    @staticmethod
    def post(request, id):
        delete_job = Job.objects.get(id=id)
        delete_job.delete()

        return HttpResponse(200)


class EditNote(SuccessMessageMixin ,generic.UpdateView):
    model = Notes
    template_name = 'job_search/pages/edit-note.html'
    fields = ['short_description', 'note', 'is_insight']
    success_url = "/fulldetails/{related_job_id}"
    success_message = 'Note successfully edited!!!!'

    def get_form_class(self):
        return NoteForm


class EditInsight(generic.UpdateView):
    model = Notes
    template_name = 'job_search/pages/edit-insight.html'
    fields = ['short_description', 'note', 'is_insight']
    success_url = '/insights'

    def get_form_class(self):
        return NoteForm
