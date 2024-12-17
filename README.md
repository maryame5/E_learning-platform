E-Learning Platform
Introduction
My name is Maryame El Khalfi, a student at the National Institute of Statistics and Applied Economics in Morocco. As a student, I frequently work with web applications such as Google Classroom, Microsoft Teams, and Zoom—platforms where teachers share courses and educational content with students. Inspired by these tools, I decided to create a custom e-learning web application called "e-Learning" as my final project.
This application is designed to manage users with different roles:
•	Admins: Manage the system and view global statistics.
•	Teachers: Create subjects, add courses, view enrolled students, and track engagement.
•	Students: Enroll in subjects, view courses, and track opened courses.
•	Normal Users: View subjects  without logging in.
The project incorporates Django for the backend, SQL for database management, and JavaScript for interactivity.
Key Features
1. User Roles
•	Admin:
o	View statistics about all subjects and the number of enrolled students.
•	Teacher:
o	Create subjects with a name and description.
o	Add courses for each subject with:
	Name
	Content
	Documents (optional
	Images (optional)
o	Delete any course by providing the subject and course name.
o	View statistics on their profile:
	Total subjects created.
	Total students enrolled in their subjects.
o	Access a "My Subjects" page that lists only their created subjects.
•	Student:
o	View available subjects and enroll in the ones they want to study.
o	View and interact with course content, including documents and images.
o	Courses are automatically marked as "opened" when accessed, and these opened courses are displayed on the student's profile page for easy tracking.
o	Access a "My Enrolled Subjects" page to view the subjects they are enrolled in.
•	Normal User:
o	Can view subjects  without logging in.
2. Profile Page
•	User Profiles display the following information:
o	Username
o	Email Address
o	A customizable bio indicating the user’s role.
	Example: “You are a teacher” or “You are a student.”
•	Editable Profile:
o	Users can edit their username, email address, and profile photo.
o	A default profile image is provided but can be modified anytime.
•	Student-Specific Feature:
o	Students can track opened courses on their profile page. This ensures they don’t revisit already accessed content.

3. Statistics and Tracking
•	Teachers can view statistics in their profile, such as:
o	Total subjects created.
o	Number of students enrolled in each subject.
•	Admins can see all subjects and the total number of students enrolled.
•	Students can track opened courses in their profile for better organization.

4. Comments System
•	Logged-in users (students, teachers, and admins) can add comments to a course page.
•	Comments are displayed instantly without requiring a page refresh.

5. Subjects and Courses
•	Teachers can add subjects with descriptions and attach multiple courses under each subject.
•	Students can browse, enroll, and view subjects and their courses.

Distinctiveness and Complexity
Distinctiveness
This project is distinct from my previous projects because of the following new features:
1.	Profile Statistics: Teachers can view the number of students enrolled in their subjects, and admins can monitor all subjects and engagement.
2.	Opened Courses Tracking: Students can track which courses they have already viewed on their profile page.
3.	Editable Profile: Users can edit their profile information, including uploading a custom profile photo.
4.	Role-Specific Functionality: Each type of user (Admin, Teacher, Student) has unique features tailored to their role.
5.	Document and Image Management: Courses can include files and images that are displayed seamlessly on the course page.
Complexity
Developing this project involved several challenges that demonstrate its complexity:
1.	Role-Based User Management: Differentiating between admins, teachers, students, and normal users required careful design of models, logic, and views.
2.	Tracking Opened Courses: Implementing a feature to mark and display "opened courses" involved database updates and logic to ensure the correct courses are tracked for each student.
3.	File and Image Handling: Allowing teachers to upload documents and images and displaying them within courses added complexity, particularly in ensuring proper file management and rendering.
4.	Interactive Comments: Building an instant commenting system required integrating Django with JavaScript for real-time updates.
5.	Editable Profiles: Enabling users to modify their profile information and upload photos involved forms, validation, and file management.

Project Files and Structure
E_learning/: Main Django application folder.
1.	models.py: Contains models for Users, Subjects, Courses, Enrolled Subjects, and Comments, Opened course .
2.	views.py: Handles logic for displaying pages, adding courses, managing subjects, and processing user actions.
3.	urls.py: Defines the URL routes for the application.
4.	templates/:
1.	layout.html: Main layout for all pages.
2.	profile.html: User profile page displaying statistics, editable options, and opened courses (for students).
3.	subjects.html: Page to view and enroll in subjects.
4.	course.html: Page to display course content, including comments and uploaded documents.
5.	Create_course.html: Page displays the form where the teacher can create a new course.
6.	Create_subject.html: Page where can a teacher create a new subject.
7.	Delete_course.html: page where the teacher can delete a course.
8.	Enrolled_subject.html: Page displays the enrolled subject
9.	My_subject.html: Page displays the subjects creating by a teacher
10.	Editprofile.html: Page where any user logged in can modify he’s information.
11.	Index.html: Page displays all subjects
12.	Login.html: Page where register users can login again
13.	Register.html: Page where new users can register and choose their role
14.	Not_authorized.html: when a non authorized user trying to access a page he will render to this page
5.	static/: Contains CSS and JavaScript files.
6.	Media: contains uploaded media like documents ,and images. 
