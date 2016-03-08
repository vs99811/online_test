from django.conf.urls import patterns, url

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^forgotpassword/$', 'password_reset', name="password_reset"),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'password_reset_confirm', name='password_reset_confirm'),
    url(r'^password_reset/mail_sent/$', 'password_reset_done',
        name='password_reset_done'),
    url(r'^password_reset/complete/$', 'password_reset_complete',
        name='password_reset_complete'),
)
urlpatterns += patterns('yaksh.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'user_login'),
    url(r'^quizzes/$', 'quizlist_user'),
    url(r'^results/$', 'results_user'),
    url(r'^start/$', 'start'),
    url(r'^start/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'start'),
    url(r'^quit/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'quit'),
    url(r'^intro/(?P<questionpaper_id>\d+)/$', 'intro'),
    url(r'^complete/$', 'complete'),
    url(r'^complete/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            'complete'),
    url(r'^register/$', 'user_register'),
    url(r'^(?P<q_id>\d+)/$', 'question'),
    url(r'^(?P<q_id>\d+)/check/$', 'check'),
    url(r'^(?P<q_id>\d+)/check/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$',\
            'check'),
    url(r'^intro/$', 'start'),
    url(r'^(?P<q_id>\d+)/(?P<attempt_num>\d+)/(?P<questionpaper_id>\d+)/$', 'show_question'),
    url(r'^enroll_request/(?P<course_id>\d+)/$', 'enroll_request'),
    url(r'^self_enroll/(?P<course_id>\d+)/$', 'self_enroll'),

    url(r'^manage/$', 'prof_manage'),
    url(r'^manage/addquestion/$', 'add_question'),
    url(r'^manage/addquestion/(?P<question_id>\d+)/$', 'add_question'),
    url(r'^manage/addquiz/$', 'add_quiz'),
    url(r'^manage/editquiz/$', 'edit_quiz'),
    url(r'^manage/editquestion/$', 'edit_question'),
    url(r'^manage/addquiz/(?P<quiz_id>\d+)/$', 'add_quiz'),
    url(r'^manage/gradeuser/$', 'show_all_users'),
    url(r'^manage/gradeuser/(?P<username>.*)/(?P<questionpaper_id>\d+)/$',
        'grade_user'),
    url(r'^manage/gradeuser/(?P<username>.*)/$', 'grade_user'),
    url(r'^manage/questions/$', 'show_all_questions'),
    url(r'^manage/showquiz/$', 'show_all_quiz'),
    url(r'^manage/monitor/$', 'monitor'),
    url(r'^manage/showquestionpapers/$', 'show_all_questionpapers'),
    url(r'^manage/showquestionpapers/(?P<questionpaper_id>\d+)/$',\
                                                    'show_all_questionpapers'),
    url(r'^manage/monitor/(?P<questionpaper_id>\d+)/$', 'monitor'),
    url(r'^manage/user_data/(?P<username>.*)/(?P<questionpaper_id>\d+)/$',
        'user_data'),
    url(r'^manage/user_data/(?P<username>.*)/$', 'user_data'),
    url(r'^manage/designquestionpaper/$', 'design_questionpaper'),
    url(r'^manage/designquestionpaper/(?P<questionpaper_id>\d+)/$',\
                                                        'design_questionpaper'),
    url(r'^manage/designquestionpaper/automatic/(?P<questionpaper_id>\d+)/$',\
                                                    'automatic_questionpaper'),
    url(r'^manage/designquestionpaper/automatic$', 'automatic_questionpaper'),
    url(r'^manage/designquestionpaper/manual$', 'manual_questionpaper'),
    url(r'^manage/designquestionpaper/manual/(?P<questionpaper_id>\d+)/$',\
                                                        'manual_questionpaper'),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/$',
        'show_statistics'),
    url(r'^manage/statistics/question/(?P<questionpaper_id>\d+)/(?P<attempt_number>\d+)/$',
        'show_statistics'),
    url(r'manage/courses/$', 'courses'),
    url(r'manage/add_course/$', 'add_course'),
    url(r'manage/course_detail/(?P<course_id>\d+)/$', 'course_detail'),
    url(r'manage/enroll/(?P<course_id>\d+)/(?P<user_id>\d+)/$', 'enroll'),
    url(r'manage/enroll/rejected/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        'enroll', {'was_rejected': True}),
    url(r'manage/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$', 'reject'),
    url(r'manage/enrolled/reject/(?P<course_id>\d+)/(?P<user_id>\d+)/$',
        'reject', {'was_enrolled': True}),
    url(r'manage/toggle_status/(?P<course_id>\d+)/$', 'toggle_course_status'),
    url(r'^ajax/questionpaper/(?P<query>.+)/$', 'ajax_questionpaper'),
    url(r'^ajax/questions/filter/$', 'ajax_questions_filter'),

)
