# scalable_online_judge
Online judge for programmers, where they can solve problems and submit there code for evaluation in different programming languages.

PROJECT DESIGN BREAKDOWN 
AIM: Build a scalable OJ for coders  
 
UI screens/routes (Task 1) {4-5 days}:  
  Login Page: To authorize the user for login  
  Admin Page: Some extended features for admin (Using default Django admin). 
  Home Page: Has a list of problems and a filter option to sort them based on solved status or difficulty. 
  Problems Page: When clicked on any problem on the above page, takes you here; this page has the problem name, description, input field to code, selection dropdown                  to pick programming language, submit button and a dynamic banner to display the verdict. 
  Submission Page: Linked to the Problems page, which takes you to view your submissions of that particular problem. Shows submission time-stamps for each                              submission. 
  [Bonus] Profile Page : To display the basic information, performance ,score and problems solved by logged in user. 
 
Design and configure Database (SQL)(Task 2) {3-4 days}:  
  ● Users:  
    UserId(default)  
    User_name 
    Hashed_password 
    total_score: float  
  ● Problems:  
    ○ problemId (Auto-Incremented) 
    ○ description: CharField  
    ○ difficulty: CharField  
    ○ solved_status: CharField(solved/unsolved)  
    ○ Score: float  
  ● Test cases:  
    ○ ProblemId (foreign key)  
    ○ Input: CharField  
    ○ Output: CharField  
  ● Submission:  
    ○ problemId (foreign key)  
    ○ Timestamp: Date  
    ○ Verdict: CharField  
 
 
Design RESTful APIS(Task 3){2-3 days}:  

1. GET: problem sorting API with pagination-10 to sort problems based on solved status or difficulty.   
2.  POST : submit solution API  
  2.1 Get the test cases(Input and output) for the problem from the test cases  Table. 
  2.2 Evaluate the submission code in your local compiler from Django view. (Learning about subprocess command) compare the outputs from the compiler result to the       output of the test cases in db. 
  2.3 Save the verdict for this submission in db  
3. GET: fetch the verdict API to show in problems page  
4. GET: fetch problems API in home page  
5. GET: fetch the list of submission to a problem (prev submission)  
 
Code evaluation system (Task 3) : 

docker : setup a docker container for the specific compiler(eg:- docker container  
          with GCC installed: https://hub.docker.com/_/gcc)  
          docker run — name my-gcc -d gcc  
          Evaluate the code in the Docker container using the docker exec command  
          (https://docs.docker.com/engine/reference/commandline/exec/) 
Sandbox :
    Isolate -> https://github.com/ioi/isolate  
    Libsandbox -> https://github.com/openjudge/sandbox 
 
 


