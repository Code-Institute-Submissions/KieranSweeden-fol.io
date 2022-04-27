# <img src="readme/images/general/fol.io-short-logo-readme-header.png" height="25"> fol.io Testing

Within this markdown file, you'll find information regarding bugs, their fixes and the testing process of fol.io.

<a href="https://folio-web-app.herokuapp.com/" target="_blank">Link to live deployment of fol.io</a>

To navigate back to the README file, [click here](README.md).

## Contents

## User Stories

## Bugs

### Fixed

The following are bugs that I have dealt with & fixed.

#### (403) Forbidden CSRF Verification Failed

I encountered an issue when first logging into the Django admin console where it would present a 403 status code page, stating that the current URL did not match any of the trusted URL's.

<details>
<summary>Read Fix</summary>

After googling the issue, I found a couple of Stack Overflow answers that helped me understand the issue and what needed to be done in order to fix it. Those are listed here:

- https://stackoverflow.com/a/70572093/1560726
- https://stackoverflow.com/a/71194288/15607265

It seems that versions of Django that are 4 and above, require the <code>CSRF_TRUSTED_ORIGINS</code> setting within settings.py.

Once I inserted this setting within my settings.py file with my respective URL, the bug was fixed.

</details>

#### django.core.exceptions.ImproperlyConfigured: Application labels aren't unique

When adding the account app to the folio project, I encountered an issue where django would not accept applications with labels that are identical. It became apparent that naming an app 'account' was problematic due to an app already existing with that name (which I assume to be the allauth account app).

<details>

<summary>Read Fix</summary>

Numerous Stack Overflow posts were made regarding this problem in Django. The one's I found most helped were the following:

- https://stackoverflow.com/a/24319562/15607265
- https://stackoverflow.com/a/59377036/15607265

To fix this issue, the app itself needed to be configured using the __init__.py file. Within this file, using the AppConfig class provided by Django, the name & label of the app was changed so Django's loader would interpret it as unique. This can be seen below:

```python

    class AccountConfig(AppConfig):
        """
        Changes the label for this app as the account name already
        exists within django. Without this, django will throw an
        ImproperlyConfigured error.
        """
        name = 'account'
        label = 'folio_account'

```

To use this class, we then needed to inform Django that the default configuration for the account app is the AccountConfig class show above, using the DEFAULT_APP_CONFIG variable shown below:

```python

    DEFAULT_APP_CONFIG = 'account.__init__.AccountConfig'

```

With the app configuration completed, all that was left to do was to include this config file within the INSTALLED_APPS list within folio's settings.py file.

```python

    INSTALLED_APPS = [
        ...
        'account.__init__.AccountConfig'
        ...
    ]

```

</details>

#### Class "UserAccount" has no objects member

When referring to the UserAccount model and the objects within it, a linting error would appear informing me that the class doesn't contain an objects member.

<details>

<summary>Read Fix</summary>

Despite being a relatively minor problem as it was a linting issue, this was likely going to be a common error found within the linting reports. For this reason, I thought to fix it within the early stages of development.

The solution was found after reading over this Stack Overflow post:

- https://stackoverflow.com/questions/45135263/class-has-no-objects-member

The issue was promptly fixed after applying the following argument within the workspace settings:

```json

 "python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
    ]

```

</details>

#### 403 Forbidden CSRF verification failed

When attempting to create an AJAX request that is involved with the saving of projects attached to a particular folio, the server would return with a 403 forbidden CSRF verification failed error.

<details>

<summary>Read Fix</summary>

After reading [this answer](https://stackoverflow.com/a/6170377/15607265) to a Stack Overflow post, I became aware of the fact that the CSRF middleware token had to be attached to the data within the request. The problem with this solution however was that it was using jQuery and I felt no need to add an entire JavaScript library to this project to complete this minor task.

During some more research, I came across [this answer](https://stackoverflow.com/a/66331048/15607265) to a Stack Overflow post which was more suited to my use case. Although jQuery was used again, this time the CSRF token was added to the header of the AJAX request, which is something I am able to do with standard JavaScript.

Using the request header code shown below, I was able to fix this issue.

```javascript

    const CSRF_TOKEN = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    request.setRequestHeader("X-CSRFToken", CSRF_TOKEN);

```

</details>

#### Project not being added to folio

When attempting to add a project to a folio, the change was not being made within the database.

<details>

<summary>Read Fix</summary>

In order to update the status of a folio being a parent to a project, a status of "is_attached" is sent to the server from the client-side via AJAX. The implementation of AJAX was utilised as forms currently exist for the projects for actions such as update & delete and using a form for the "is_attached" functionality would mean having forms within forms, which is not valid HTML.

The data being sent to the server was a list of projects containing the project's ID and an "is_attached" boolean value. It was the project's ID which was causing the problem, as it was being sent to the server as a string.

Further down the view, the list of projects was being sorted using the project ID as a key. Given it was a string rather than an int, it was not being sorted as intially intended. After applying the code below, the fix was made.

```python

    def sort_by_id(entity):
    """
    Returns the id of provided entity
    which can be used for sorting purposes
    """
    return int(entity['id'])

```

</details>

#### CSRF verification failed: Request aborted

After starting up the application server via Gitpod and submitting a form within the application, an error is presented informing me that the CSRF verifcation process has failed and that the request has been aborted.

<details>

<summary>Read Fix</summary>

When launching the project workspace via Gitpod, there's a chance that the URL given for a new Gitpod workspace session could be slightly different to the URL used in a previous workspace session.

This means that hard-coding the CSRF trusted origin would lead to problems, as the string provided would likely not match the URL given within the next Gitpod workspace session.

To fix this, the Gitpod workspace url environment variable was taken & partitioned into seperate sections. Inserting "*8000-" inbetween the "https://" and "kieran" partitions and combining the partions with f strings, meant that the CSRF trusted origin would be dynamically created and would match any given workspace session for this particular project.

Given that this is an issue that would only occur in development, this was also wrapped in an if statement to ensure this would only occur within e development environment.

The code that fixed this is provided below:

```python
    # CSRF
    if "DEVELOPMENT" in os.environ:

        url_partitions = os.environ.get('GITPOD_WORKSPACE_URL').partition('kieran')

        csrf_string = (
            f"{url_partitions[0]}*8000-"
            f"{url_partitions[1]}{url_partitions[2]}"
        )

        CSRF_TRUSTED_ORIGINS = [(csrf_string)]

```

</details>

#### Heroku Error: Items could not be retrieved, Internal server error

When attempting to connect my GitHub account to Heroku so I could assign the Heroku app to folio's GitHub repository, instead of providing me with a list of my GitHub repositories, Heroku threw an error stating "Items could not be retrieved, Internal server error".

<details>

<summary>Read Fix</summary>

After researching the error being given, it was clear after reading [this Stack Overflow answer](https://stackoverflow.com/a/71895325/15607265) that the GitHub connect feature was temporarily disabled due to a security breach. As the answer suggests, the fix was to use the Heroku CLI instead.

[This Stack Overflow answer](https://stackoverflow.com/a/71905270/15607265) tremendously helped in quickly getting the Heroku CLI up and running with the git repository.

Although other bugs presented themselves after this, the error in which the repo could not communicate with Heroku was now fixed.

</details>

#### ERROR: Could not build wheels for backports.zoneinfo...

Despite now having communication with Heroku via their CLI, the build attempts by Heroku were failing due to a backports.zoneinfo related issue. After reading [this Stack Overflow answer](https://stackoverflow.com/a/71735458/15607265), it was clear that the version of Python that Heroku installs by default was not working with the folio codebase.

<details>

<summary>Read Fix</summary>

To rectify the issue according to [this Heroku article](https://devcenter.heroku.com/articles/python-runtimes), a runtime.txt file containing a specified version of Python was required, to inform Heroku as to which version of Python it should install instead. To find out the particular version of Python I was working with, I entered <code>python -V</code> within the console which gave the following result:

```bash
python-3.8.11
```

Inserting this within the runtime.txt file rectified the issue after adding and commiting the file the repository.

</details>

#### No Folios match the given query

When the user has no folios within their account and they attempt to view their folio library, django provides a query related error where "No Folios match the given query".

<details>

<summary>Read Fix</summary>

After researching this error online, it became apparent that it was an obvious user error on my part. This was due to the use of the get_list_or_404 shortcut function to retrieve folios. If no folios were found with the given query, it would throw an error which was not the intended functionality.

To resolve this issue, it was simply replacing the get_list_or_404 function with the following syntax:

```python
folios = Folio.objects.filter(author_id=request.user)
```

</details>


### Known

The following are bugs that are still present within the current build of fol.io.

## User Testing

## File Validation

## Defensive Programming

## Testing Functionality

## Accessibility & Performance