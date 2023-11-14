function uploadComment() {
    // 필수 입력 필드들을 확인합니다.
    let commentName = document.getElementById('commentName').value;
    let commentPassword = document.getElementById('commentPassword').value;
    let commentInput = document.getElementById('commentInput').value;
    let postID = window.location.pathname.split('/')[2];

    // 필수 입력 필드들 중 하나라도 비어 있으면, 경고를 띄우고 폼 제출을 방지합니다.
    if (!commentName || !commentPassword || !commentInput || !postID) {
        alert('Please fill in all required fields.');
        event.preventDefault(); // 폼 제출을 방지합니다.
        return; // 함수를 종료합니다.
    }

    // FormData 객체 생성
    let formData = new FormData();

    // FormData에 텍스트 데이터 추가
    formData.append('commentName', commentName);
    formData.append('commentPassword', commentPassword);
    formData.append('commentInput', commentInput);
    formData.append('postID', postID);

    uploadCommentFetch(formData);
}

function uploadCommentFetch(formData) {
    fetch('/listPage/post', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if(data['STATUS'] == true){
            alert('Comment Success!');
            location.href = window.location.pathname
        }else if(data['STATUS'] == false){
            alert('Comment Faild...');
        }
    })
}

function promptDelete() {
    let password = prompt("Please enter your password for verification:");
    let postID = window.location.pathname.split('/')[2];

    if (password) {
        // FormData 객체 생성
        let formData = new FormData();

        // FormData에 텍스트 데이터 추가
        formData.append('password', password);
        formData.append('postID', postID);

        deletePostFetch(formData);
    } else {
        alert("Password are required to delete the post!");
    }
}

function deletePostFetch(formData) {
    fetch('/listPage/del/post', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if(data['STATUS'] == true){
            alert('Delete Success!');
            location.href = '/listPage'
        }else if(data['STATUS'] == false){
            alert('Delete Faild...');
        }
    })
}