# <img src="readme/images/general/fol.io-short-logo-readme-header.png" height="25"> fol.io

<img src="readme/images/surface/folio-readme-header.png">

Fol.io is a CRUD-based web application written with Python using the Django framework.

Fol.io allows it's users to create folios that are viewable to potential employers who do not have accounts with folio. Users can create, update, delete and swap various portfolio snippets that are often found within tech-oriented portfolios, empowering them to create various folios that present them in their best light to fulfill numerous job descriptions found in the tech industry.

Using Stripe to purchase fol.io licenses, users can "publish" these folios for the outside world to see, helping them on their job searching journeys.

<a href="https://folio-web-app.herokuapp.com/" target="_blank">Link to live deployment of fol.io</a>

## Table of Contents

* [UX](#ux)
    + [Strategy](#strategy)
        - [The Problem](#the-problem)
        - [The Solutions](#the-solutions)
        - [The Objectives](#the-objectives)
        - [The Audience](#the-audience)
        - [User Stories](#user-stories)
        - [Potential Features](#potential-features)
    + [Scope](#scope)
        - [Current Features](#current-features)
        - [Future Features](#future-features)
    + [Structure](#structure)
    + [Skeleton](#skeleton)
        - [Wireframes](#wireframes)
        - [Database Schema](#database-schema)
            * [AllAuth User Model](#allauth-user-model)
            * [UserAccount](#useraccount)
            * [Folio](#folio)
            * [Project](#project)
            * [Skill](#skill)
            * [Profile](#profile)
            * [License Purchase](#license-purchase)
    + [Surface](#surface)
        - [Visual Language](#visual-language)
            * [Colour](#colour)
            * [Typography](#typography)
            * [Imagery & Identity](#imagery---identity)
* [Technology](#technology)
    + [Languages](#languages)
    + [Libraries, Frameworks and API's](#libraries--frameworks-and-api-s)
    + [Applications](#applications)
    + [Others](#others)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
    + [Code](#code)
        - [Credited](#credited)
        - [Inspiration](#inspiration)
    + [Research](#research)
    + [Media](#media)
        - [Images](#images)
* [Acknowledgements](#acknowledgements)

## UX

### Strategy

#### The Problem

It's well documented within the IT industry that it's becoming increasingly difficult for businesses to fill their IT positions with qualified personnel.

#### The Solutions

[This article](https://www.codingame.com/work/blog/find-developers/top-it-recruitment-challenges/) by Nathalie Figui??re, which dissects these challenges utilizing survey data given from developers & current IT HR personnel, proposes a variety of solutions to help combat this. The first three solutions Figui??re provides, are the ones that are relevant to this application, those being the:

- Removal of IT degree requirements
- Consideration of non-traditionally educated developers
- Broadening of searching for candidates

Despite degree's remaining a key requirement within most company recruitment processes, the removal of degree requirements is [becoming an increasingly more common stance](https://www.cnbc.com/2018/08/16/15-companies-that-no-longer-require-employees-to-have-a-college-degree.html). However, as [this article](https://www.businessinsider.com/apple-google-hire-jobs-without-degree-experts-say-college-important-2020-10?r=US&IR=T) suggests, experts still say that a college degree remains the best bet in landing a well paid tech job.

The consideration of non-traditionally educated developers regards those who are self-taught, that learned their development skills from other forms of educational resources such as videos within YouTube or online courses hosted by Udemy etc. Figui??re dives deeper within [this article](https://www.codingame.com/work/blog/tech-recruiting/why-you-should-hire-self-taught-developers/), presenting reasons why self-taught developers should be considered, some notable reasons being that self-taught developers are:

- Eagerly motivated given their education is driven by themselves.
- Likely more communicative as they're often integrating within online tech communities.
- Adaptable in taking on new tech, not relying on tech skills acquired in school.
- Natural problem solvers given they've likely learned from hitting roadblocks & chicanes during their learning.

The broadening of searching for candidates, suggests that businesses should employ multichannel recruitment strategies, utilizing online platforms such as LinkedIn, Indeed or community events such as hackathons or coding contests.

A conflicting aspect to an application like this, is that developers are obviously able to create their own portfolio to highlight their work. One negative to this however, is that it takes a lot of time to create a portfolio and aspiring developers who are self-taught are likely to be working full-time, meaning they have limited time available. A platform that presents their talents & work whilst being quick & easy to update would be beneficial, as they can focus their efforts on producing side-applications that are of more interest to potential employers.

It's also common place to tailor a CV for a particular job, so that what the employer sees is relevant to the job specification. It's likely a self-taught developer will be applying to numerous vacancies and adjustments will need to be made in order to present themselves in their best light to the employer. [This post](https://jobhelp.campaign.gov.uk/right-for-the-role-5-ways-to-tailor-your-cv-to-the-job-description/) suggests the following are resume elements that should be changed per application to target particular vacancies:

- The introduction
- Keywords
- Employment history

#### The Objectives

Taking these points into consideration, the application should aim to:

- Highlight the strengths & skills of self-taught developers.
    - The content developers create regarding themselves should be front & centre, acting as the focal point and the application itself should take a backseat when the content is being viewed from employers.
- Position itself stylistically alongside other alternative hiring sources.
    - The application should sport a UI that's familiar to these existing platforms, utilizing the conventions these platforms have created to make the application's UI easily learnable.
- Be a speedy & easy way for aspiring developers to update what they've previously done, what they're currently up to and their future goals.
    - The speedy nature requires as few clicks/actions as possible for the individual to achieve their respective goal with the application.
- Make the user's portfolio alterations simple and quick, saving them time and enabling them to apply for more vacancies.

#### The Audience

The target audience for this application are self-taught developers, who are likely participating in a career change whilst working full-time and would benefit from a quick and easy way to present their work and skills to potential employers.

Following B2C considerations, it's important that the application sports a simple, clean & modern brand look and targets their struggle with time management, being presented as a fast & effective solution to present their talents. The target audience is also likely in not justifying their purchasing decisions resulting in impulse buying, so the purchasing mechanism needs to be quick and easy.

#### User Stories

As a self-taught and aspiring developer, I want to be able to:

**Account Management**

- Register an account.
- Log in to the account I've registered.
- Change my account details.
- Reset the password of my account.
- See the amount of folio licences I have.

**Folio Management**

- Create a brand new folio.
- Edit an existing folio within my library.
- Toggle as to whether I want a folio to be viewable or not to the outside world.
- View the folio in it's live state despite being published or not.
- Delete a folio from my library.

**Snippet Management**

- Create snippets (that represent common portfolio sections) that can be re-used throughout my libary of folios.
- Select which snippets make it to each respective folio.
- Modify & update the content of a snippet within my collection.
- Delete a snippet from my collection.

**Billing**

- Insert my billing details and have them be saved to my account.
- Make a license purchase.
- Find information regarding previous license purchases I've made.

As an employer interested in the developer, I want to be able to:

**Folio Viewing**

- View a potential employee's folio.
- See what they're currently up to.
- Investigate what projects they've already created.
- Find out what skills they current posess.
- Discern what their future aspirations are.
- Promptly know how I can contact them.
- Message the author of the folio directly.

#### Potential Features

Below is a table of opportunities/problems that could potentially be included within the MVP of the application:

| Opportunities/Problem       | Importance | Feasibility |
|-----------------------------|------------|-------------|
| Account Management          | 5          | 5           |
| Purchase Portfolio Licences | 5          | 4           |
| Responsive Design           | 4          | 5           |
| Keyword Checklist           | 2          | 3           |
| Portfolio Viewer            | 5          | 5           |
| Themes                      | 2          | 3           |
| Creation Suite              | 5          | 4           |

[Return to Table of Contents &#8679;](#table-of-contents)

### Scope

#### Current Features

The following is the list of features that will be included within the MVP of the application with reasons as to why:

- Account Management
    - Important data relating to the user such as their portfolios, account details and billing information will need to be tied to their account, making this an integral feature within the application.

- Purchase of Portfolio Licenses
    - The purchase of portfolio licences is what will achieve the application's business goals. Without it, in a realistic setting the application is not financially viable, therefore it's important to be present within the MVP of the application.

- Responsive Design
    - The application should be available to all possible users, no matter what device they have available to them. Although users are more likely to use desktop devices when using the application, focusing on this group would lessen the financial gains the application could potentially receive. For this reason and because it's expected by most users in this day and age, this feature should be present within the MVP of the application.

- Portfolio Viewer
    - For the application to be useful to the target audience, their potential employers need to be able to view their portfolio's (provided they have a licence). Without this, it would render the application as useless to the target audience, therefore it's integral that it should be present within the MVP of the application.

- Creation Suite
    - The user will need to add content to their portfolio's, therefore a creation suite of sorts where they're able to add text content, links, images etc. will be absolutely necessary. For this reason, it's important that this feature makes it into the MVP of the application.

#### Future Features

The following is a list of features that will be left for future release of the application with reason as to why:

- Keyword Checklist
   - The keyword checklist feature is where a customer can paste a job description into a text area and the feature will extract the keywords from the job description and add them to a checklist. The user is then able to view this checklist when creating their portfolio, making sure they address all the job criteria.
    - Although useful, this is essentially an additional time saving feature and is not integral to the application's core functionality. For this reason, this will be left for a later update of the application.

- Themes
    - The themes feature allows the user to further personalize their portfolio with a particular styling of their choice.
    - Although this would help the user differentiate themselves, it's not integral to the core functionality of the application. For this reason, it will be left for a future update of the application.

- Duplicate folios/snippets
    - This feature will be a must have for the next release of the application. This is where a user is able to create a duplicate of a folio or snippet they already have.

[Return to Table of Contents &#8679;](#table-of-contents)

### Structure

In order to gain a better understanding as to how the application will be divided in terms of user scope, core functionality & it's contained apps, a spreadsheet was created which can be viewed here: https://docs.google.com/spreadsheets/d/1DoUd4K2EvncLdwspScBpB-SKJV1YkRlqaxTjj5FSsyo/edit?usp=sharing.

Although this spreadsheet is analysing the application at a high level, the structure is visually clear which will help maintain focus on the core aspects of the application during development.

Regarding information architecture, the chosen navigational schema is the Tree Structure, due to its reduction of complexity, and it's familiarity with most users which will aid in learnability.

Click below to view this tree structure:

<details>

<summary>View Tree Structure of Application</summary>

<img src="readme/images/structure/folio-tree-structure.png">

</details>

The tree structure presents the core pages that are closely tied to user objectives. These pages will of course be expanded into multiple, however the tree structure will remain despite this.

Following common practice, along with the tree structure there will be top navigation that will collapse within a hamburger menu for mobile users. Taking advantage of this industry standard will help make the application's UX friendly and approachable to the user.

[Return to Table of Contents &#8679;](#table-of-contents)

### Skeleton

#### Wireframes

During the Skeleton phase of this UX section, I created a set of wireframes using [Balsamiq](https://balsamiq.com/) in order to gain a better understanding of how certain pages would be presented.

These wireframes can be viewed from a seperate markdown file [here](WIREFRAMES.md).

#### Database Schema

In order to gain a better understanding as to what the models would be along with their relationships within folio's databases, a database schema was created with [dbdiagram.io](https://dbdiagram.io/home) which can be viewed below:

<details>

<summary>View Database Schema</summary>

<img src="readme/images/skeleton/database-schema.png">

</details>

At the time of writing, dbdiagram does not support the visual representation of many to many relationships between database records. With that being said, a line representing a relationship is presented within the diagram for purely visual purposes and I will best explain what the relationship is in writing.

> id AutoField for the models are not present within the code as the field is automatically created in the background. The inclusion of the id field is used purely for visual purposes in explaining the relationships clearer.

##### AllAuth User Model

The application will make use of the user model that's contained within the django allauth app, using it's email, username and password fields along with the id that's automatically given when created. The allauth user model will simply act as the fields that are necessary to register and log in to the app whilst being the foreign key for all other models within the application.

##### UserAccount

The UserAccount has a one to one relationship with the allauth user model, as an authenticated user will only have one account that's unique to them. The UserAccount model wraps all additional information regarding the user that is not directly linked to the authentication process through the app. This includes account details that are used for pre-filling forms and folios along with billing details that will act as defaults for user convenience when making license purchases. The UserAccount model will also contain the number of licenses a user has, which is referred to primarily within the library app to make sure a user has enough licenses in their account before they attempt to publish a folio.

##### Folio

A folio has a foreign key (i.e. a many to one) relationship with the allauth user model, as an authenticated user can have many folios however a folio can only have one authenticated user as it's author. The last updated and date created fields are automatically filled after particular save events relating to the folio and their purpose is to be used for sorting purposes so user's can sort their folios by last updated or the date they were created.

> Time constraints unfortunately meant that the intended functionality of having mutliple sorting methods wasn't feasible. At the moment the date created is the default and the last updated sorting feature will be applied within a later release of fol.io.

The id of the folio model is what snippet models such as the Project, Skill and Profile models will refer to when making database queries.

The model also holds an is published boolean field which will store the published status of the folio. This is toggled by an authenticated user providing they have at least 1 folio license left to use within their respective user account model.

##### Project

A project has a foreign key (i.e. a many to one) relationship with the allauth user model, as an authenticated user can have many projects however a project can only have one authenticated user as it's author. The project model also has a many to many relationship with the folio model, as a project can have a relationship with multiple folios and a folio can have a relationship with multiple projects.

##### Skill

A skill within the database has a foreign key (i.e. a many to one) relationship with the allauth user model, as an authenticated user can have many skills however a skill can only have one authenticated user as it's author. There's also a a many to many relationship with the folio model, as a skill can have a relationship with multiple folios and a folio can have a relationship with multiple skills.

##### Profile

The profile model has a foreign key (i.e. a many to one) relationship with the allauth user model, as an authenticated user can have many profiles however a profile can only have one authenticated user as it's author. Like the previous snippets mentioned before it, there's a a many to many relationship with the folio model, as a profile can have a relationship with multiple folios and a folio can have a relationship with multiple profiles.

##### License Purchase

The license purchase model has a foreign key (i.e. a many to one) relationship with the allauth user model, as an authenticated user can be the purchaser of multiple license purchases however the license purchase can only have one authenticated user as it's purchaser. This model has fields that hold information and address details that are only applicable to that purchase, so the address and user details could be billed to someone else that's not the authenticated user.

This also holds the amount of licenses the user has purchased which is what's used to increment the number of licenses field found within the user account model.

Given that the purchase is processed via Stripe, a record of the Stripe purchase ID is also kept so it can be referred to when presenting a successful purchase view to the user.

The license purchase model will also hold a unique order number using the UUIDv4 hash method. This is to simulate an order number that's often given to a customer when making a purchase, so the customer can later refer to the order number when attempting to contact regarding a recent purchase.

[Return to Table of Contents &#8679;](#table-of-contents)

### Surface

#### Visual Language

A visual language is integral to conveying additional context to the user, about a given piece of text or action. Given that this is considered good practise in UX design, fol.io will have this integrated within it's design philosophy.

Throughout the application, it will present primary, secondary & tertiary actions with each sporting a unique respective design. This will allow for easy learning of the UI, making the application approachable within a short period of time.

Fol.io will also utilize various typography styles to represent a sense of structural hierarchy within the application. Providing the styling is consistent throughout the application, this will provide a sense of comfort to the user as they will be familiar as to where they are within the application.

##### Colour

First and foremost, fol.io's goal is to highlight its users, so its colour palette should reflect this in not being too vibrant or distracting to employers. With this in mind, fol.io's colour palette should be largely conservative, only containing a black, white and feature colour, that will be used to provide context within the application such as what page they're currently on.

Considering the applications users would be aspiring/current developers who are likely comfortable with modern IDE's sporting a dark mode and recruiters within companies who are looking at screens for large portions of time, the background of the application should be the black within the colour palette, making the application comfortable to view for its users.

In terms of the feature colour, after researching colour psychology and the power colour has on people's emotions and impressions when viewing a product, I decided the feature colour should be within yellow & orange. This is due yellow's optimistic nature, which connects nicely with the goals that fol.io has and orange's energetic feel which also feeds into fol.io's goals well. The feature colour containing yellow will also be useful due to its ability in grabbing the user's attention, which makes it a perfect fit as the colour that'll support primary actions within the application.

After experimenting with [Coolors](https://coolors.co/), the final colour palette is as follows:

<img src="readme/images/surface/colour-palette.png">

As can be seen, the intensity of the black & white colours have been decreased slightly to make text more readable within the application. Speaking of readability, according to [Colour Contrast Checker](https://colourcontrast.cc/), the yellow/orange colour passes all WCAG guidelines when contrasted with the black colour, as can be seen below:

<img src="readme/images/surface/yellow-black-wcag-contrast.png">

This was a calculated decision, given that the feature colour will be used for buttons and feature text within the application. With this in mind, it was important that the guidelines were followed for accessibility reasons.

##### Typography

Taking into account that the intention of fol.io is to be integrated within the hiring processes in IT recruitment, its typography should communicate that it's users immediately. With this in mind, a serif font would be suitable as it's often used in formal environments due to its elegant & classic feel. On the contrary to this however, the IT industry is modern, which suggests a sans-serif font should be utilized due to their minimal & modern feel.

Taking both of these points into account, fol.io will utilize two fonts, one being serif and the other being sans-serif. This allows fol.io to position itself as a modern application that's visually comfortable in formal environments.

What's important however, is that the use of the fonts is calculated and followed within a typography system. This will help prevent the application from being visually unappealing and provide a sense of structure & contextual hierarchy throughout the application.

After experimenting with various fonts within the [Google Font Library](https://fonts.google.com/), I ended up with [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville#standard-styles) as the serif font and [Inter](https://fonts.google.com/specimen/Inter) as the sans-serif font.

Taking into account the chosen colour palette and fonts, the typography system that will be followed throughout the site will be as follows:

<img src="readme/images/surface/typography-system.png">
<sub><sup>The buttons below represent the buttons in their regular state. The buttons above represent the buttons in their active state.</sup></sub>

As can be seen from the image above, the following will be followed:

- Headings will sport the Libre Baskerville serif font.
- Body text will be presented using the Inter sans-serif font.
- The link representing the current page will be bolder than the other links and sport an underline featuring the feature colour. This will clearly communicate to the user what page they're currently on.
- The primary button will sport the main feature colour as intended.
- The secondary button will sport the white colour.
- The tertiary button will simply have an underline to seperate itself from the body text.

##### Imagery & Identity

It's integral that fol.io is consistent with its imagery, as it all contributes to the overall brand of fol.io.

With this in mind, fol.io will sport "programming-isms" in its design philosophy. Minor details such as the removal of capitalization within its headings, relating to syntax within programming which is often lowercase.

Another relation to programming fol.io presents is the name fol.io in of itself. Programming names are often shortened for conciseness, hence going from portfolio to folio and the .io is coincidentally an opportunity that presented itself as it could easily be inserted within folio. This minor addition immediately informs the user that fol.io is very much a tech-oriented application.

With this taken into account, the logo will be as follows:

<img src="readme/images/surface/folio-readme-header.png">

The logo shown on mobile devices which will also be used as a favicon will be as follows:

<img src="readme/images/surface/fol.io-short-logo-readme-header.png">

[Return to Table of Contents &#8679;](#table-of-contents)

## Technology

### Languages

The following languages were used during the development of fol.io:

- HTML
- CSS
- JavaScript
- Python

### Libraries, Frameworks and API's

The following libraries & applications were utilized during the development of fo.io:

- [Django](https://www.djangoproject.com/)
    - The Django python framework was utilized to quickly create and manage fol.io.

- [Stripe](https://stripe.com/en-gb)
    - The Stripe API was used to process online test card payments to open up functionalit within the application.

- [Bootstrap 5](https://getbootstrap.com/)
    - The Bootstrap 5 CSS framework was utilized to quickly create element & component designs during the development of fol.io.

- [Google Fonts](https://fonts.google.com/)
    - Google Fonts was used to import the fonts utilized by fol.io.

- [Google Material Icons](https://fonts.google.com/icons)
    - Google Material Icons was used to import visual icons utilized by fol.io throughout the application.

- [Font Awesome Icons](https://fontawesome.com/)
    - Font Awesome icons was used for icons not present within Google Material Icons (e.g social media icons).

- [animate.css](https://animate.style/)
    - animate.css was used to quickly create animations within fol.io.

- [clamp.js](https://github.com/josephschmitt/Clamp.js)
    - Clamp.js was used to clamp down specific pieces of text found throughout the folio app to guarantee that pages do not too cluttered with unnecessary text.

### Applications

The following applications listed were utilized during the development of fol.io:

- [Gitpod](https://www.gitpod.io/)
    - Gitpod was used as the IDE of choice for the development of fol.io.

- [draw.io](https://github.com/jgraph/drawio-desktop/releases/tag/v16.5.1)
    - draw.io was used to create the flowchart for fol.io's structure in its MVP state.

- [Coolors](https://coolors.co/)
    - The colour palette generator within Coolors was used to create the colour palette for fol.io.

- [Colour Contrast Checker](https://colourcontrast.cc/)
    - The Colour Contrast Checker application was used to check the colour contrast between the colours in fol.io's colour palette.

- [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create wireframes during the skeleton phase of fol.io.

- [dbdiagram.io](https://dbdiagram.io/home)
    - dbdiagram.io was used to create the visual representations of the application's database schema.

- [favicon.io](https://favicon.io/favicon-converter/)
    - favicon.io was used to create favicon icons for this project.

- [Affinity Designer](https://affinity.serif.com/en-gb/designer/)
    - Affinity Designer was used to create numerous graphics that were used within folio.

- [GitHub Wiki TOC Generator](https://ecotrust-canada.github.io/markdown-toc/)
    - The GitHub Wiki TOC Generator was used to quickly generate table of contents for various markdown files within this repository.

- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)
    - The W3C Markup Validation Service tool was used to validate the source html of the pages contained within the application.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - The W3C CSS Validation Service tool was used to validate the base.css file that's shared amongst all html files within the application.

- [JSHint](https://jshint.com/)
    - The JSHint tool was used to validate the custom-made JavaScript files that are used throughout the application.

- [PEP8 Online](http://pep8online.com/)
    - The PEP8 online python validator was used for sanity checking that the python files were indeed valid. This was carried out as python validation was carried out throughout the development process using the onboard IDE linters such as PyLint and PEP8.

- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - Google Chrome's in-built Lighthouse app was used to test the accessibility and performance of the application.

### Others

- [Heroku](https://dashboard.heroku.com/login)
    - Heroku was used as the platform to host the application live.

- [AWS](https://aws.amazon.com/)
    - AWS was used to host static files and images for the project whilst in deployment

[Return to Table of Contents &#8679;](#table-of-contents)

## Testing

To keep the README.md file concise, all information regarding bugs and testing during the development of fol.io was documented within the [TESTING.md](TESTING.md) file.

[Return to Table of Contents &#8679;](#table-of-contents)

## Deployment

To keep the README.md file concise, the deployment section has been given it's own unique markdown file. To view deployment procedures, please click [here](DEPLOYMENT.md).

[Return to Table of Contents &#8679;](#table-of-contents)

## Credits

### Code

#### Credited

The following links are to the sources of code written by others that's found within the folio codebase.

- [clamp.js](https://github.com/josephschmitt/Clamp.js)
    - Clamp.js was used to clamp down specific pieces of text found throughout the folio app to guarantee that pages do not too cluttered with unnecessary text.

- [Bootstrap tooltip code](https://getbootstrap.com/docs/5.0/components/tooltips/#example-enable-tooltips-everywhere)
    - The JavaScript found within the "Enable tooltips everywhere" section was used to enable tooltips throughout the entire application.

- [Looping through errors within django form to display error messages](https://stackoverflow.com/a/24273898/15607265)
    -  Partial amount of this code was copied and used within login page of the application.

#### Inspiration

The following are links to sources of programming information that I found tremendously useful during the development of fol.io. Code was not directly taken from these sources of information, they were simply helpful in guiding me towards my intended goals during the development process.

- [Django Tutorials Playlist](https://www.youtube.com/playlist?list=PLXmMXHVSvS-DQfOsQdXkzEZyD0Vei7PKf)
    - Credit: [Pretty Printed](https://www.youtube.com/c/PrettyPrintedTutorials)
    - I found a bunch of these Django specific videos really useful during the development of the application. It helped deepen my understanding of database relationships, using advanced queries within Django and helped with the use of AWS for database storage.

- [Django Tutorial (Create a Blog)](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
    - Credit: [The Net Ninja](https://www.youtube.com/c/TheNetNinja)
    - I found this playlist of tutorials particularly useful as it was bringing concepts together within a full mini project. I found another perspective in building a project very useful when used in conjunction with the course material with Code Institute.

### Research

The following links are sources that were used to further understand the problems that needed to be solved during the pre-production stages of folio.

- [Top 4 IT Recruitment Challenges (and How to Overcome Them!)](https://www.codingame.com/work/blog/find-developers/top-it-recruitment-challenges/) by Nathalie Figui??re.
    - This article provided solutions backed by data, which helped provide further understanding of the IT recruitment problems and how to fix them.

- [Google, Apple and 12 other companies that no longer require employees to have a college degree](https://www.cnbc.com/2018/08/16/15-companies-that-no-longer-require-employees-to-have-a-college-degree.html) by Courtney Connley.
    - This article presented facts regarding the increasing trend of removing degree requirements within large tech corporations.

- [Apple and Google are looking for new ways to hire people without college degrees ??? but experts say college might still be your best bet for landing a high-paying tech job](https://www.businessinsider.com/apple-google-hire-jobs-without-degree-experts-say-college-important-2020-10?r=US&IR=T) by Lisa Eadicicco.
    - This article presented information regarding the fact that despite the increasing trend of removing degree requirements, experts still recommend it within the tech field.

- [6 Reasons Why You Should Hire Self-Taught Developers](https://www.codingame.com/work/blog/tech-recruiting/why-you-should-hire-self-taught-developers/) by Nathalie Figui??re.
    - This article presented a variety of strength's self-taught developers have, which was useful in discerning what should be front and centre for a user's portfolio.

- [RIGHT FOR THE ROLE: 5 WAYS TO TAILOR YOUR CV TO THE JOB DESCRIPTION](https://jobhelp.campaign.gov.uk/right-for-the-role-5-ways-to-tailor-your-cv-to-the-job-description/)
    - This post presents 5 ways in which resumes should be changed to target a particular job, which was useful in deciding which portfolio elements should be able to moved within the portfolio.

### Media

#### Images

- [Man Using 3 Computers](https://www.pexels.com/photo/man-using-3-computers-4974914/)
    - Credit: [Olia Danilivich](https://www.pexels.com/@olia-danilevich/)
    - This image was used for the home page of the application

- [Man Using Laptop Computer](https://www.pexels.com/photo/man-using-laptop-computer-2102415/)
    - Credit: [Djordje Petrovic](https://www.pexels.com/@djordje-petrovic-590080/)
    - This image was used for the home page of the application

- [Man Gets The Job](https://www.pexels.com/photo/man-gets-the-job-5439381/)
    - Credit: [Tima Miroshnichenko](https://www.pexels.com/@tima-miroshnichenko/)
    - This image was used for the home page of the application.

- [Photo of Woman Smiling While Using Laptop](https://www.pexels.com/photo/photo-of-woman-smiling-while-using-laptop-4458419/)
    - Credit: [Yan Krukov](https://www.pexels.com/@yankrukov/)
    - This image was used for the home page of the application.

[Return to Table of Contents &#8679;](#table-of-contents)

## Acknowledgements

Within this section of the README file, I'd like to thank:

- My mentor Sammy, for their guidance and excitement that encourages me to go a step further when developing web applications.
- Code Institute for their  Diploma in Web Application Development course that has tremendously helped me in learning the fundamentals and advanced topics in Full Stack web development.

[Return to Table of Contents &#8679;](#table-of-contents)