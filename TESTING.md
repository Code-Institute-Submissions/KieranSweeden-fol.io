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

#### No 'Access-Control-Allow-Origin' header is present on the requested resource

When viewing the deployed app on Heroku, certain JavaScript based functionality was not working due to the base.js file not being loaded in properly. According to the browser console, it was a CORS related issue where a required header was missing.

<details>

<summary>Read Fix</summary>

After researching this issue, numerous fixes were presented including the use of django-cors middleware to attach CORS headers to files. These fixes didn't work in my case however.

What I found puzzling was that over JavaScript files were being loaded in fine, however the base.js file was not. Due to this, I investigated the codebase and noticed I had accidently left the attribute of type="module" within the script tag that was loading base.js. After removing this attribute, the problem was fixed.

</details>

#### Navbar was wider than html body & overflow-x wasn't working on mobile devices

When looking at the site via the mobile device viewer on Google Chrome, the viewport could be moved slightly to the right which was un-intentional in fol.io's design. Along with the unexpected behaviour of being able to slightly shift the viewport to the right, the elements on the page weren't positioned correctly.

<details>

<summary>Read Fix</summary>

Attempts at fixing this with CSS classes in Bootstrap 5 and other CSS workarounds found through Stack Overflow, did not provide the desired outcome in fixing the max width of certain elements to the width of the body element.

The fix however did come to light via [this Stack Overflow answer](https://stackoverflow.com/a/41407863/15607265) which suggests the inclusion of "user-scalable=no" within the viewport meta tag. After making this change, the elements flowed and fitted on the page as expected.

</details>

#### Pylint - Django was not configured error

For each page, a pylint error was present at the top of the page during a GitPod session. Although this had little to no effect on the project itself, from a testing staandpoint it was distracting.

<details>

<summary>Read Fix</summary>

In order to solve this problem, after reading [this Stack Overflow answer](https://stackoverflow.com/a/68346742/15607265), it became clear that a .pylintrc file was needed.

After creating the file and inserting the pylint commands found within the Stack Overflow answer, this soon resolved the issue and allowed me to focus on certain files with legitimate errors.

The commands can be found below:

```
[MASTER]
load-plugins=pylint_django
django-settings-module=fol.io.settings
```

</details>

#### Character count too long (100)

After realising that the character count for various descriptions within models needed to be increased, the changes were made and migrated with no issue on the development server. However, an error was occuring on Heroku when submitting a new snippet to the database as the description lengths were too long.

<details>

<summary>Read Fix</summary>

It was self explanatory that it was migration-based on the Heroku deployment side and after looking at [this Stack Overflow post](https://stackoverflow.com/a/54793985/15607265), it provided a helpful way in getting the fix sorted promptly.

After performing the following commands below, the issue was fixed.

```bash
heroku run python manage.py migrate suite zero
heroku push heroku main
heroku run python manage.py migrate
```

</details>

#### Duplicate id's

As I'm using various models containing their respective forms for various objects, after looking through the HTML validator it became clear that a problem had arisen where an object such as a folio had an "update_folio" model with the same id as an "update_folio" from another folio.

<details>

<summary>Read Fix</summary>

A fix for this was making use of the prefix feature within django that allows a user to prefix the id's within forms, in this example specifically, folio update forms.

```python
for folio in folios:
    folio.form = CreateFolioForm(
        instance=folio,
        prefix=f"folio-{folio.id}"
    )
```

Using this meant that each folio model had an individual id and was not causing any errors regarding HTML validation. One problem this did mean however was the prefixes meant that the forms were no longer valid when being submitted to the server.

After looking at [this Stack Overflow answer](https://stackoverflow.com/a/22210263/15607265), a good option was to make a copy of the query dictionary and add to it the required fields by the form (in this case "name" and "description") which enabled the form to be valid. Although this feels like a hack, due to time constriants this was the best option unfortunately. The copy of the query dictionary can be seen below:

```python
post = request.POST.copy()
    post['name'] = post[f"folio-{folio_id}-name"]
    post['description'] = post[f"folio-{folio_id}-description"]
    form = CreateFolioForm(post, instance=folio_in_db)
```

</details>

### Known

The following are bugs that are still present within the current build of fol.io.

## User Testing

To help with the user friendiness of fol.io, I decided to conduct a user test where I handed fol.io to a family member who's tech-savvy (whom I will call tester from now on) and asked them to perform a set of tasks within the site. Although it could be considered more appropriate to put this in front of someone such as a web developer, I thought it was useful to put this in front of someone who is only vaguely familiar with programming, as it would better challenge how well the application informed it's user as to what to do next. The thinking was, if someone who has a general idea on development can get around the application, a web developer or at least someone of that calibre in their understanding of tech would certainly understand the application.

What was clear when first looking at the site, was that the general concept of the application was not being communicated well to the tester. They were initially confused by the suite and the naming of it. It wasn't clear to them what the functionality for this portion of the app was for. Only when I explained the suite app in a different light, did they begin to understand the functionalityi that it provided. With this in mind, I started from square one in terms of the word content presented within the home page as this is the opportunity to inform the user as to what fol.io contains. Myself and the tester agreed that directly addressing the apps by name (such as Suite, Library, License Store) alongside the functionality they could provide helped communicate the concept of the application better.

Another problem that the tester observed was the inconcistency in language regarding particular entities found within the application. An example of which is alternating between "profiles" and "profile snippets" which is absolutely understandable. With this in mind, during the later portion of development, a consistent effort was made to present concepts and entites within fol.io in a consistent manner to make it easier to explain. THese changes will hopefully makie the learning process whilst learning fol.io easier than it was previously.

One issue that was also raised was the lack of guidance when a folio didn't contain any content for a respective reason. This could include a name not being presented or a default profile picture being shown. The tester recommended that rather than informing the user of a problem, it would be better to be directed to the source of the problem and given guidance as to how to fix it. I agreed with the tester's comments, however the trouble of time became a greater issue and given that it was a nice to have rather than an absolutely necessary piece of functionality, it was placed on the "if time allows" to-do list. It's definitely a feature that should appear in a future release of fol.io.

## File Validation

### HTML

### CSS

Below you will find the results for the CSS validation results for the base.css file that is shared amongst all html pages within the application.

<details>

<summary>View CSS Results</summary>

<img src="readme/images/validation/css/css-validation-check.png">

</details>

Despite the positive result, there were 3 warnings given regarding web prefixes:

<details>

<summary>View CSS Warnings</summary>

<img src="readme/images/validation/css/css-validation-warnings.png">

</details>

Given that this is intentional for webkit supported browsers to make the application more aesthetically pleasing, this was not deemed an issue for the application.

### JavaScript

### Python

## Defensive Programming

Following conventional web development standards, all sensitive information such as id's and keys are kept hidden from source control. This was achieved with the use of Gitpod's environment variables feature and the config variables that are found within the settings tab of the Heroku app.

"Internal" pages all require a logged in session. This is achieved via the use of django's allauth middleware that comes pre-packaged with the python framework. Without this session, the user is re-directed to the log-in page or is presented a custom made error page that fits the design of fol.io and also provides functionality that takes the user back to a reasonable place within the application.

All views that are directly linked to the management of objects stored within the database can only be managed if the current user is the "author" of the object. This is to protect the potential case where one could delete or modify another user's folio or project/skill/profile snippet without being the author.

## Testing Functionality

## Accessibility & Performance