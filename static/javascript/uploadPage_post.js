function uploadPost() {
    let projectImages = document.getElementsByClassName('projectImage');
    let projectLink = document.getElementById('projectLink').value;
    let projectGithub = document.getElementById('projectGithub').value;
    let userInstagram = document.getElementById('userInstagram').value;

    // 필수 입력 필드들을 확인합니다.
    let projectName = document.getElementById('projectName').value;
    let projectOneLineIntroduction = document.getElementById('projectOneLineIntroduction').value;
    let projectIntroduction = tinyMCE.get('projectIntroduction').getContent();
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    // 필수 입력 필드들 중 하나라도 비어 있으면, 경고를 띄우고 폼 제출을 방지합니다.
    if (!projectName || !projectOneLineIntroduction || !projectIntroduction || !email || !password) {
        alert('Please fill in all required fields.');
        event.preventDefault(); // 폼 제출을 방지합니다.
        return; // 함수를 종료합니다.
    }

    // FormData 객체 생성
    let formData = new FormData();

    // FormData에 텍스트 데이터 추가
    formData.append('projectName', projectName);
    formData.append('projectOneLineIntroduction', projectOneLineIntroduction);
    formData.append('projectIntroduction', projectIntroduction);
    formData.append('projectLink', projectLink);
    formData.append('projectGithub', projectGithub);
    formData.append('userInstagram', userInstagram);
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
    .then(response => response.json())
    .then(data => {
        if(data['STATUS'] == true){
            alert('Post Success!');
            location.href = '/'
        }else if(data['STATUS'] == false){
            alert('Post Faild...');
        }
    })
}
