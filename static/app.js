const selectElement = (s) => document.querySelector(s);

selectElement('.bookform').style.display = "none";



selectElement('.open').addEventListener('click', () =>{
    selectElement('.nav-list').classList.add('active');
});

selectElement('.close').addEventListener('click', () =>{
    selectElement('.nav-list').classList.remove('active');
});


selectElement('.book-before').addEventListener('click', () =>{
    selectElement('.book-before').style.display = 'none';
    selectElement('.bookform').style.display = "block";
});

selectElement('#form').addEventListener('submit', (e) =>{
//    e.preventDefault();
    alert('Your Booking Has been Placed ... Our Sales Assistant will contact you in a Moment..');
})
