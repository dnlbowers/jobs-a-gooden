from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Job, PinnedJobs, Notes
from .forms import NoteForm, AddJobForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Taken https://www.djangoforge.dev/guides/page-titles/
class PageTitleViewMixin:
    title = ""

    def get_title(self):
        """
        Return the class title attr by default
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class AddJob(SuccessMessageMixin, PageTitleViewMixin, generic.CreateView):
    """
    This view is used to add a job to the database.
    """
    form_class = AddJobForm
    template_name = 'job_search/pages/add-job.html'
    success_url = reverse_lazy('add_job')
    success_message = 'Your Job Advert has been Successfully Submitted and is'\
        ' Awaiting Admin Approval'
    title = "Add a Job"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        Successful form submission will redirect the user back to the
        add job page.
        """

        super(AddJob, self).form_valid(form)
        return redirect('add_job')


class AddInsight(SuccessMessageMixin, PageTitleViewMixin, generic.CreateView):
    """
    This view is used to add a job to the database.
    """
    form_class = NoteForm
    template_name = 'job_search/pages/add-insight.html'
    success_url = reverse_lazy('insights')
    success_message = 'Your insight has been addned Successfully'
    title = "Add an Insight"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        Successful form submission will redirect the user back to the
        add job page.
        """
        form.instance.user = self.request.user
        form.instance.is_insight = self.request.is_insight = True
        super(AddInsight, self).form_valid(form)
        return redirect('insights')


class JobList(generic.ListView):
    """
    This view is used to display a list of public approved jobs.
    """
    model = Job
    paginate_by = 6
    template_name = 'job_search/pages/job-list.html'
    context_object_name = 'jobs'
    queryset = Job.objects.filter(
        status=1, approved=True
    ).order_by('-date_posted')


class FullJobSpec(PageTitleViewMixin, View):
    """
    This view is used to display a full job spec, including notes/insights.
    It also display the form to create notes and insights.
    """

    def get(self, request, id, *args, **kwargs):
        """
        Retrieves the job spec and related notes/insights from the database.
        """

        queryset = Job.objects.filter(status=1, approved=True)
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
                'note_form': NoteForm(),
                'title': 'Job Details',
            },
        )

    def post(self, request, id, *args, **kwargs):
        """
        This method is called when a POST request is made to the view
        via the note creation form.
        """

        queryset = Job.objects.filter(status=1, approved=True)
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
            new_note = Notes.objects.get(id=note.id)
            messages.success(request, 'Note/insight successfully added')
            return HttpResponseRedirect(reverse_lazy(
                'add_note',
                kwargs={'pk': new_note.id, 'id': id}
            ))

        else:
            note_form = NoteForm()
            messages.error(
                request,
                'Please be sure to enter a short description and a note.'
            )

        return render(
            request,
            'job_search/pages/job-details.html',
            {
                'author': author,
                "job": job_spec,
                "pinned": pinned,
                'notes': notes,
                'note_made': True,  # boolean to to use as conditional
                'note_form': NoteForm(),
                'title': 'Job Details',
            },
        )


class PinJob(View):
    """
    This view is used to toggle the pinned status of a job.
    """

    def post(self, request, id):
        """
        When pin jon toggle is toggled this method is called
        to update the relevant many2many fields in the database
        """

        # get the status of the toggle from post request in JS file
        status = True if request.POST['status'] == 'true' else False
        # Identify the job being toggled
        job = Job.objects.get(id=id)
        # identify the users pinned job database table
        pinned = PinnedJobs.objects.get(user=request.user)
        user_notes = Notes.objects.all().filter(user=request.user)

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
            for note in user_notes:
                if note.related_job == job and note.is_insight is False:
                    note.delete()

        return HttpResponse(200)


class PinnedPosts(generic.ListView):
    """
    This view is used to display a list of pinned jobs.
    """

    model = PinnedJobs
    paginate_by = 6
    template_name = 'job_search/pages/pinboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        """
        Gets only the pinned jobs for the current user.
        """

        # get all pinned posts by user
        pinned = PinnedJobs.objects.get(user=self.request.user)
        # get all jobs from the many to many list
        jobs = pinned.pinned_jobs.all()
        return jobs


class DisplayInsights(generic.ListView):
    """
    This view is used to display a list of insights for a job.
    """

    model = Notes
    paginate_by = 6
    template_name = 'job_search/pages/insights.html'
    context_object_name = 'insights'
    queryset = Notes.objects.filter(is_insight=True).order_by('-date_created')

    def get_queryset(self):
        """"
        filters insights to be specific to the current user
        """
        return super().get_queryset().filter(user=self.request.user)


class DeleteNote(View):
    """
    This view is used to delete a note from the database.
    """
    # delete note from database (check why the params work like they do)
    @staticmethod
    def post(request, id):
        """"
        Gets the note id from the post request and deletes the note.
        """
        delete_note = Notes.objects.get(id=id)
        delete_note.delete()
        return HttpResponse(200)


class DeleteJob(View):
    """"
    This view deletes a job from the database.
    returns a httpresponse when successful
    """
    # delete job from database (check why the params work like they do)
    @staticmethod
    def post(request, id):
        """
        Gets the job id from the post request and deletes the job.
        returns a httpresponse when successful
        """
        delete_job = Job.objects.get(id=id)
        delete_job.delete()

        return HttpResponse(200)


class EditNote(SuccessMessageMixin, PageTitleViewMixin, generic.UpdateView):
    """
    This view is used to edit a note in the database.
    directly from the job details page, and display a alert as feedback
    """

    model = Notes
    template_name = 'job_search/pages/edit-note.html'
    fields = ['short_description', 'note', 'is_insight']
    success_url = "/fulldetails/{related_job_id}"
    success_message = 'Note Successfully Updated'
    title = 'Edit Note'

    def get_form_class(self):
        """
        Gets the form class for the edit note view.
        """
        return NoteForm


class EditInsight(SuccessMessageMixin, PageTitleViewMixin, generic.UpdateView):
    """
    This view is used to edit a note marked as an insight in the database.
    directly from the insights page, and display a alert as feedback
    """
    model = Notes
    template_name = 'job_search/pages/add-insight.html'
    fields = ['short_description', 'note', 'is_insight']
    success_url = '/insights'
    success_message = 'Insight Successfully Updated'
    title = 'Edit Insight'

    def get_form_class(self):
        """
        Gets the form class for the edit insight view.
        """
        return NoteForm

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        Successful form submission will redirect the user back to the
        add job page.
        """
        form.instance.user = self.request.user
        form.instance.is_insight = self.request.is_insight = True
        super(EditInsight, self).form_valid(form)
        return redirect('insights')


class EditJob(SuccessMessageMixin, PageTitleViewMixin, generic.UpdateView):
    """
    This view is used to edit a job in the database,
    and displays an alert as feedback
    """
    model = Job
    template_name = 'job_search/pages/add-job.html'
    success_url = '../{id}'
    fields = '__all__'
    success_message = 'Job Successfully Updated'
    title = 'Edit Job'

    def get_form_class(self):
        """
        Gets the form class for the edit job view.
        """
        return AddJobForm
