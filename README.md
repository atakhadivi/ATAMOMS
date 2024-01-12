# ATAMOMS

the project definition
using flask for project
read rss from the porn videos website and filter mom word and save them to database
show in the home page the thumbnail of the video and title and clickable
when the click happened if in database have embed show the page with embed video else redirect user to the source web page
have search function
categorize the videos into the categories i've added by me based on if the word in category have in the rss add to database with those categories
create suggestion system for visitor based on the history and use cookie for this
add like , dislike , report function
create our network page to show the the sources i got the data from them

This is a comprehensive to-do list for project, detailing the various steps required to build the application.

## Table of Contents

1. [Set Up the Development Environment](#1-set-up-the-development-environment)
2. [Design the Project Architecture](#2-design-the-project-architecture)
3. [Create the Flask Application](#3-create-the-flask-application)
4. [Set Up the Database](#4-set-up-the-database)
5. [Define the Project Models](#5-define-the-project-models)
6. [Implement the Views and Templates](#6-implement-the-views-and-templates)
7. [Integrate with the RSS Feed](#7-integrate-with-the-rss-feed)
8. [Implement Filtering and Category Management](#8-implement-filtering-and-category-management)
9. [Add Database Support](#9-add-database-support)
10. [Implement the Search Functionality](#10-implement-the-search-functionality)
11. [Implement the Suggestion System](#11-implement-the-suggestion-system)
12. [Add User Interaction Features](#12-add-user-interaction-features)
13. [Create the Our Network Page](#13-create-the-our-network-page)
14. [Implement Error Handling and Security Measures](#14-implement-error-handling-and-security-measures)
15. [Test the Application](#15-test-the-application)
16. [Deploy the Application](#16-deploy-the-application)
17. [Update the Project Documentation](#17-update-the-project-documentation)

## 1. Set Up the Development Environment

- [x] Install Python: Download and install the latest version of Python from the official website.
- [x] Install Flask: Open your terminal and run `pip install Flask`.
- [x] Install SQLAlchemy: Run `pip install SQLAlchemy`.
- [x] Install Requests: Run `pip install requests`.

## 2. Design the Project Architecture

- [x] Outline the components of the application.
  - Web Scraper: This component is responsible for reading RSS feeds from the porn videos website and filter out entries that contain the word "mom". The filtered entries will then be saved to a database. 2 Database: This component stores the filtered entries from the web scraper. Each entry should include the thumbnail of the video, the title, and the URL of the video.
  - Frontend: This component is responsible for displaying the entries from the database on the home page. When a user clicks on an entry, the application will check if the embed URL is available in the database. If it is, the application will display the video on a separate page. Otherwise, the user will be redirected to the source web page.
  - Search Function: This component allows users to search for entries in the database based on keywords.
  - Categorization: This component categorizes the entries in the database based on predefined categories. When an entry is added to the database, the application will check if any of the categories match the content of the entry. If a match is found, the entry will be added to the corresponding category.
  - Suggestion System: This component uses cookies to track user activity and suggest entries based on their browsing history.
  - Like/Dislike/Report Function: This component allows users to provide feedback on the entries in the database. This feedback can be used to improve the quality of the entries and the overall user experience.
  - Network Page: This component displays information about the sources from which the application obtains data.
- [x] Define the routes and URL patterns.

  1.  Home Page

  - Shows a list of video thumbnails and titles, which are clickable
  - When a user clicks on video, it checks if the video is already in the database If the video is in the database, it the video using the embed code
  - If video is not in the database, it redirects the user to the source website
  - Has a search function to search for videos by keyword
  - Uses cookies to suggest videos based on the user's viewing history
  - Allows users to like, dislike, or report videos

  2.  Network Page

  - Shows a list of the websites that the videos are sourced from
  - Provides links to each website

  3.  Database Management

  - Automatically detects text files and performs LF normalization
  - Reads RSS feeds from porn video websites and filters for the word "mom"
  - Saves the filtered videos to the database
  - Categorizes the videos based on keywords added by the administrator

- [x] Plan the views and templates.

  1.  Home Page Template

  - Displays a list of video thumbnails and titles
  - Has a search bar for searching videos
  - Displays a message if the video is not in the database and redirects the user to the source website
  - Displays the video using the embed code if it is in the database
  - Has like, dislike, and report buttons for each video
  - Displays suggested videos based on the user's viewing history

  2.  Network Page Template

  - Displays a list of websites that the videos are sourced from
  - Provides links to each website

  3.  Database Management Template

  - Has a form for adding keywords to categorize videos
  - Displays a list of videos in the database
  - Allows the administrator to filter videos by keyword
  - Has a button to save filtered videos to the database

  Here are the suggested views:

  1.  Home Page View

  - Displays the home page template
  - Handles the search function
  - Checks if the video is in the database and displays it using the embed code or redirects the user to the source website
  - Saves the user's viewing history to a cookie
  - Handles the like, dislike, and report functions
  - Displays suggested videos based on the user's viewing history

  2.  Network Page View

  - Displays the network page template
  - Provides links to each website

  3.  Database Management View

  - Displays the database management template
  - Allows the administrator to add keywords to categorize videos
  - Filters videos by keyword
  - Saves filtered videos to the database

- [x] Design the database schema and models.
  1.  Video
      -id
      -title
      -url
      -thumbnail
      -tags
      -embed
      -category_id
      -category
      Database schema:
      Users table:
  2.  Category
      -id
      -name
      -description
      -videos

## 3. Create the Flask Application

- [x] Set up a new Python file (e.g., `app.py`) to create the Flask application instance.
- [x] Configure the application by setting the `SECRET_KEY` and enabling `DEBUG` mode.

## 4. Set Up the Database

- [x] Choose a suitable database system SQLite
- [x] Create a new database to store the video and category data.
- [x] Initialize SQLAlchemy to establish a connection with the database.

## 5. Define the Project Models

- [x] Create the `Video` model to represent the videos.
- [x] Create the `Category` model to represent the categories.
- [x] Define the relationships between the models using SQLAlchemy's ORM.

## 6. Implement the Views and Templates

- [x] Create a `videos` view to render the video listings.
- [ ] Create a `video` view to render the individual video details and embeddable video player.
- [ ] Design the templates (`videos.html` and `video.html`) to display the video data.

## 7. Integrate with the RSS Feed

- [ ] Use the Requests library to fetch the RSS feed from the porn videos website.
- [ ] Parse the feed using an RSS parsing library (e.g., `feedparser`) to extract

## 8. Implement Filtering and Category Management

- [ ] Add filtering functionality to the video listings.
- [ ] Implement category management features (e.g., create, edit, and delete categories).

## 9. Add Database Support

- [ ] Store the video and category data in the database.
- [ ] Implement pagination for the video listings.

## 10. Implement the Search Functionality

- [ ] Add a search bar to the video listings page.
- [ ] Implement search functionality using a search library (e.g., `Whoosh`).

## 11. Implement the Suggestion System

- [ ] Implement a recommendation system based on user preferences.
- [ ] Display suggested videos on the video listings page.

## 12. Add User Interaction Features

- [ ] Implement user authentication and authorization.
- [ ] Add features for users to like, dislike, and comment on videos.

## 13. Create the Our Network Page

- [ ] Design the layout and content for the "Our Network" page.
- [ ] Display links to related websites and social media profiles.

## 14. Implement Error Handling and Security Measures

- [ ] Implement custom error pages for common HTTP errors (e.g., 404 and 500).
- [ ] Implement security measures to protect against common web attacks (e.g., XSS and CSRF).

## 15. Test the Application

- [ ] Write unit tests for the application's functionality.
- [ ] Test the application on different browsers and devices.

## 16. Deploy the Application

- [ ] Choose a suitable web hosting provider (e.g., Heroku, AWS, or Google Cloud).
- [ ] Configure the application for production deployment.
- [ ] Deploy the application and test it in a live environment.

## 17. Update the Project Documentation

- [ ] Update the README file with any changes made during development.
- [ ] Write user documentation for the application.
