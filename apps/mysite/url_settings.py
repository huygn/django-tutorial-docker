"""
For overriding absolute URLs.
This is a way of inserting or overriding 'get_absolute_url()' methods
on a per-installation basis.
https://docs.djangoproject.com/en/1.9/ref/settings/#absolute-url-overrides
"""

ABSOLUTE_URL_OVERRIDES = {
    'polls.question': lambda o: "/polls/{id}/{pub_date}/".format(
        id=o.id,
        pub_date=o.pub_date.strftime('%Y-%m-%d'),
        # might as well add 'o.slug' here..
    ),
}
