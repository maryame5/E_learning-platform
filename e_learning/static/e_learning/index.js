document.addEventListener("DOMContentLoaded", function() {
    const createButton = document.querySelector("#create_subject");
    const createcourse = document.querySelector("#create_course_button");
    if (createButton) {
        createButton.addEventListener("click", create());}
    if (createcourse) {
        createcourse.addEventListener("click", create_course());}
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
                'X-CSRFToken': getCookie('csrftoken') 
               
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
function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        const cookies = document.cookie.split(';');
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i].trim();
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

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
                 'X-CSRFToken': getCookie('csrftoken') 
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