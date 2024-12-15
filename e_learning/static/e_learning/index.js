document.addEventListener("DOMContentLoaded", function() {
    const createButton = document.querySelector("#create_subject");
    const createcourse = document.querySelector("#create_course_button");
    const deletebutton= document.querySelector("#deletebut");
    const commentt=document.querySelector("#commentt");
    document.querySelectorAll('.btn-outline-primary').forEach(button => {
        button.addEventListener('click', open_course);

    });
    
    if (deletebutton){
        deletebutton.addEventListener("click", deleteCourse)}
    if (createButton) {
        createButton.addEventListener("click", create());}
    if (createcourse) {
        createcourse.addEventListener("click", create_course());}
    if(commentt){
        commentt.addEventListener("click",comments())
    }
    const subjectDat = document.querySelector("#nams").value;
    const subjectData = JSON.parse(subjectDat);

    // Prepare data for the enrollment chart
    const enrollmentLabels = Object.keys(subjectData);
    const enrollmentValues = Object.values(subjectData);
    console.log(subjectData);
    console.log("111111111",enrollmentLabels);
    console.log("2222222222", enrollmentValues);
    

    // Create the enrollment chart
        const enrollmentCtx = document.querySelector('#enrollmentChart');
        if (!enrollmentCtx) {
            console.error("Canvas element not found!");
            return; // Exit if the canvas is not found
        }

        // Get the 2D context
        const ctx = enrollmentCtx.getContext('2d');
        if (!ctx) {
            console.error("Failed to get canvas context!");
            return; // Exit if the context is not available
        }


    new Chart(enrollmentCtx, {
        type: 'bar', // You can change this to 'line', 'pie', etc.
        data: {
            labels: enrollmentLabels,
            datasets: [{
                label: 'Number of Students Enrolled',
                data: enrollmentValues,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});


    
 

function create(event) {
    document.querySelector('form').onsubmit = function(event) {
        // Clear out composition fields
            event.preventDefault();
            
            const description = document.querySelector("#subject_description").value;
            const teacher = document.querySelector("#teacher").value;
            const name = document.querySelector('#subject_name').value;
            console.log("teacher:",teacher," name :",name," description:",description);
            const payload = {
                teacher: teacher,
                name: name,
                description: description
            };
      
            fetch('/create_subject', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                
               
            },
              body: JSON.stringify(payload)
            })
            .then(response =>  {
                if (!response.ok){
                    throw new Error('Network response was not ok');}
                return response.json();})
            .then(data => {
                console.log("subject created",data); 
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
            });
                };}


function create_course() {
    document.querySelector('form').onsubmit = function(event) {
    // Clear out composition fields
    event.preventDefault();
                            
    const content = document.querySelector("#content").value;
    const teacher = document.querySelector("#teacher").value;
    const name = document.querySelector('#course_name').value;
    const subject_name = document.querySelector('#subject_name').value;
    const image = document.querySelector('#course_image').value;
    const c_document = document.querySelector('#course_document').value;

    console.log("teacher:",teacher," name :",name," content:",content ," image :",image ," document :",c_document);
    const payload = {
                 teacher: teacher,
                 name: name,
                 content: content,
                 image:image,
                 
                 subject_name:subject_name
                 };
                      
     fetch('/create_course', {
             method: 'POST',
                 headers: {
                 'Content-Type': 'application/json',
                 
                                  },
                 body: JSON.stringify(payload)
                         })
                 .then(response =>  {
                 if (!response.ok){
                     throw new Error('Network response was not ok');}
                     return response.json();})
                .then(data => {
                        console.log("course created",data); 
                          })
                            .catch(error => {
                                console.error("There was a problem with the fetch operation:", error);
                            });
                                };}
                                
function deleteCourse() {
    document.querySelector('form').onsubmit = function(event) {
    event.preventDefault();
    const course_name = document.querySelector('#course_name').value;
    const subject_name=document.querySelector("#subject_name").value;

                                    // Show confirmation alert
            const confirmed = confirm("Are you sure you want to delete this course?");
                                    
            if (confirmed) {
                
                fetch('/delete_course', {
                     method: 'POST',
                     headers: {
                         'Content-Type': 'application/json', },
                     body: JSON.stringify({
                            course_name: course_name,
                            subject_name: subject_name }) })
                .then(response => {
                    if (response.ok) {
                                                // If the response is OK, show success alert
                     alert("Course deleted successfully.");
                                                // Optionally, you can refresh the page or remove the course element from the DOM
                                                // Reload the page to reflect changes
                     } else {
                                                // Handle errors
                        return response.json()
                 .then(data => { if (data.error) {
                                            // Handle error (e.g., display error message)
                      console.log(data.error);
                }
                                        
                                            })}
                                        })
                                        .catch(error => {
                                            alert("An error occurred: " + error);
                                        });
                                    }
                                }}
 function open_course(event) {
    let course_name = event.target.id;
    console.log("Course Name:", course_name); 
    const course_element  = event.target.closest('.course');
    if (!course_element) {
        console.error("Course element not found.");
        return;
    }
                                    
  fetch(`/course/${course_name}`, {
    method: 'PUT',
    headers: {
            'Content-Type': 'application/json',  
        },
    body: JSON.stringify({
    is_open: true
      })})
    .then(() => {
      console.log("open");}) 
    .catch(error => {
        console.log("There was a problem with the fetch operation:", error);

    });}
                                
                                
                                
function comments(){
    document.querySelector('form').onsubmit = function(event) {
        event.preventDefault();
        const course_name = document.querySelector('#course_name').value;
        const commen = document.querySelector("#comment").value;
        const user_name = document.querySelector('#userr').value;
        fetch("/comment", {
        
                     method: 'post',
                     headers: {
                          'Content-Type': 'application/json'},
                     body: JSON.stringify({
                           course_name:course_name,
                           commen:commen,
                           user:user_name
                           }) })
                .then(response =>  {
                     if (!response.ok){
                        console.log("Response status:", response.status);
                         throw new Error('Network response was not ok')}
                    return response.json();})
                .then(commen => {
                     console.log("commen", commen);

                    })
                .catch(error => {
                      console.log( error)})
}}            
