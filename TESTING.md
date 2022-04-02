# <img src="readme/images/general/fol.io-short-logo-readme-header.png" height="25"> fol.io Testing

Within this markdown file, you'll find information regarding bugs, their fixes and the testing process of fol.io.

[Link to deployment of fol.io]()

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


### Known

The following are bugs that are still present within the current build of fol.io.

## User Testing

## File Validation

## Defensive Programming

## Testing Functionality

## Accessibility & Performance