function uploadPost() {
    let projectName = document.getElementById('projectName').value;
    let projectOneLineIntroduction = document.getElementById('projectOneLineIntroduction').value;
    let projectIntroduction = tinyMCE.get('projectIntroduction').getContent();
    let projectImages = document.getElementsByClassName('projectImage');
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    // FormData 객체 생성
    let formData = new FormData();

    // FormData에 텍스트 데이터 추가
    formData.append('projectName', projectName);
    formData.append('projectOneLineIntroduction', projectOneLineIntroduction);
    formData.append('projectIntroduction', projectIntroduction);
    formData.append('email', email);
    formData.append('password', password);

    // 모든 이미지 필드에서 파일을 추출하여 FormData에 추가
    for (let i = 0; i < projectImages.length; i++) {
        if (projectImages[i].files[0]) {
            formData.append('projectImages', projectImages[i].files[0]);
        }
    }

    uploadFetch(formData);
}

function uploadFetch(formData) {
    fetch('/uploadPage/post', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
