**Takeaways from this class**<br>

*How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?*

Programs that are maintanable, readable and adaptable are of paramount importance to allow collaboration and inheritability as development teams change hands. No program will be maintained by the same developers. With that in mind making things easy to catch on to is important. In this class developing the Module allowed for abstracting away the CRUD functionality and ensuring that developers of the dashboard could focus on the dashboard development and less on the nuts and bolts of interacting with the database. The documentation of how the python module was created, what the code was are all readily available if that needs to be tweaked. However, it is not directly interfering or easy to introduce bugs to in this implementation. 

In the future I could use this module as a starting point for any python-based project that is interacting with a MongoDB.

*How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?*

As a Computer Scientist I approach problems by first gathering all requirements and having a thorough understanding of what clients need. My approach in this course is similar to what my approach has been in other courses, I do not jump into coding right away and make sure I understand clearly what my objectives are. It's very easy to get lost in rabbit holes with unclear objectives. In regards to database development to meet client requests, I've learned quite a bit about how to ensure secure interaction with databases from this course and am confident I can carry that abstraction and security into future projects.


*What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?*

Computer Scientists explore different applications of Programming Languages to meet dynamic and ever evolving needs of Society. We serve as a catalyst to better utilize data and computers to fulfill goals and objectives. We can greatly aid organizations and individuals to more productively handle data and enable data-informed decision making and insights. In this classes scenario , we were able to enable Grazioso Salvare to better find Rescue Dogs to train and influence the lives of 1000s in need by leveraging data analytics and a web-based dashboard.

<br><br><br><br>

**Scenario**<br>
You work for Global Rain, a software engineering company that specializes in custom software design and development. Your team has been assigned to work on a project for an innovative international rescue-animal training company, Grazioso Salvare. You have been made the lead developer on this project.

Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs can find and help to rescue humans or other animals, often in life-threatening conditions. To help identify dogs for training, Grazioso Salvare has reached an agreement with a nonprofit agency that operates five animal shelters in the region around Austin, Texas. This nonprofit agency will provide Grazioso Salvare with data from their shelters.

You meet with the client, Grazioso Salvare, and discover that they look for certain profiles in dogs to train. For instance, search-and-rescue training is generally more effective for dogs no more than two years old. Also, certain breeds of dogs are proficient at different types of rescue, such as water rescue, mountain or wilderness rescue, locating humans after a disaster, or finding a specific human by tracking their scent.

Grazioso Salvare is seeking a software application that can work with existing data from the animal shelters to identify and categorize available dogs. Global Rain has contracted for a full stack development of this application that will include a database and a client-facing web application dashboard. Users at Grazioso Salvare will access the database. The full stack development will be fully completed in Projects One and Two.

Grazioso Salvare has also requested that the code for this project be open source and accessible on GitHub so similar organizations may use and adapt it. They have asked that you also create a README file to accompany your work.

In Project One, you will complete the first phase of this development by creating a database in MongoDB that can interact with client-side code. You will also create an initial README file to accompany your code. In Project Two, later in this course, you will complete the second phase of development by updating the database, producing the dashboard, and updating the README file to explain the full stack development.


**Project One**<br>
*This Project was focused on the backend development of the web application*
We were required to create a separate user account with read write access to only the database of concern. Additionally, we were to create a module that has CRUD functionality utilizing this new user account. This allows read/write access to only the data related to the project.


I uploaded the dataset using the mongoimport tool. This demonstrates the ability to upload a .csv dataset into a mongoDB instance.
![Import Command Screenshot](Project%20Two/Resources/1_1_mongoimport.png)

I created a user account that only has read/write access to the database of concern. This enforces secure development practices.
![Import Command Screenshot](Project%20Two/Resources/2_1_user_account_creation.png)

I created a Module in Python that accesses the MongoDB Animal Collection and successfully Creates/Reads/Updates/Deletes records in the MongoDB collection. 
![Import Command Screenshot](Project%20Two/Resources/3_1_MongoCRUD_Test.png)
![Import Command Screenshot](Project%20Two/Resources/3_2_MongoCRUD_Test.png)

**Project Two**<br>
*This project was focused on the frontend development of the web application*
We were required to create an interactive dashboard for the stakeholders that allowed for navigation of the Shelter Data and Geolocation features on a map widget. Additionally we were to provide a secondary graphic that gives an insight to the distribution of breeds filtered. There were 3 different Rescue Functions, Water, Mountain Rescue and Disaster Rescue. Each of these different Rescue Types had different Breed , Sex and Age Requirements to be adopted into the program.


https://github.com/Syncert/CS_340_client_server_dev/assets/54092419/a6f07c00-0b58-41a0-9b30-d1c2d053d71c


Landing Page
![Import Command Screenshot](Project%20Two/Resources/screenshot_1.png)
Filtered to Water Rescue
![Import Command Screenshot](Project%20Two/Resources/screenshot_2.png)
Filtered to Mountain and Disaster Rescue
![Import Command Screenshot](Project%20Two/Resources/screenshot_3.png)
Filtered to 
![Import Command Screenshot](Project%20Two/Resources/screenshot_4.png)

**Getting Started**<br>
*If you'd like to install and run a copy of this MongoDB CRUD Module, detailed instructions are present in the README_MongoCRUD.docx file*

