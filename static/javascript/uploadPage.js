tinymce.init({
    selector: 'textarea#projectIntroduction',
    menubar: false,
    statusbar: false,
    plugins: [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount'
    ],
    toolbar: 'undo redo | formatselect | ' +
        'bold italic backcolor | alignleft aligncenter ' +
        'alignright alignjustify | bullist numlist outdent indent | ' +
        'removeformat | help',
    // setup 함수는 에디터의 초기화 중에 호출되는 콜백입니다.
    setup: function (editor) {
        var maxIntroductionLength = 1500;
        function updateCharacterCount() {
            var textContent = editor.getContent({ format: 'text' });
            var currentLength = textContent.length;

            // 글자 수가 최대 글자 수를 초과하면 초과하는 부분을 자릅니다.
            if (currentLength > maxIntroductionLength) {
                // 이전에 정상적으로 입력된 내용으로 되돌립니다.
                editor.undoManager.undo();
                return; // 카운터 업데이트를 방지하기 위해 여기서 리턴합니다.
            }

            // 현재 글자 수를 업데이트합니다.
            var counter = document.getElementById('projectIntroductionCounter');
            if(counter) {
                counter.textContent = currentLength + '/' + maxIntroductionLength;
            }
        }

        editor.on('init', function() {
            // 에디터 초기화 후 현재 글자 수를 업데이트합니다.
            updateCharacterCount();
        });

        // 에디터 내용이 변경될 때마다 호출될 이벤트 핸들러 등록
        editor.on('keydown', function (e) {
            updateCharacterCount();
        });

        editor.on('keyup', function (e) {
            updateCharacterCount();
        });

        editor.on('change', function (e) {
            updateCharacterCount();
        });
    }
});      

// form submit 막기
const $form = document.querySelector("form");
$form.addEventListener("submit", (event) =>{
    event.preventDefault();
});

function addImageField() {
    // 이미지 입력 필드를 포함할 div를 생성합니다.
    var container = document.createElement("div");
    container.className = 'image-upload-container';

    // input 타입 'file'을 생성합니다.
    var input = document.createElement("input");
    input.type = "file";
    input.name = "projectImages";
    input.accept = "image/*";

    // 생성된 input을 div에 추가합니다.
    container.appendChild(input);

    // 생성된 div를 form에 추가합니다.
    var form = document.getElementById("projectUploadForm");
    var addButton = document.getElementById("addImageButton");
    form.insertBefore(container, addButton);
}

function addImageField() {
    // 이미지 입력 필드의 수를 체크합니다.
    var imageFields = document.querySelectorAll('input[name="projectImages"]').length;
    var maxFields = 5;

    // 이미지 입력 필드의 수가 최대 개수보다 적으면 새 필드를 추가합니다.
    if (imageFields < maxFields) {
        var container = document.createElement("div");
        container.className = 'image-upload-container';

        var input = document.createElement("input");
        input.type = "file";
        input.name = "projectImages";
        input.className = "projectImage";
        input.accept = "image/*";

        container.appendChild(input);

        var form = document.getElementById("projectUploadForm");
        var addButton = document.getElementById("addImageButton");
        form.insertBefore(container, addButton);

        // 현재 이미지 수를 업데이트합니다.
        updateImageCounter();
    } else {
        alert('You can only add up to ' + maxFields + ' images.');
    }
}

function updateImageCounter() {
    // 현재 이미지 수를 셉니다.
    var imageFields = document.querySelectorAll('input[name="projectImages"]').length;
    var maxFields = 5;

    // 이미지 카운터 업데이트
    var imageCounter = document.getElementById("imageCounter");
    imageCounter.textContent = imageFields + '/' + maxFields;
}

// projectName 및 projectOneLineIntroductionCounter 업데이트 함수 추가
function updateTextCounter(input, counterId, maxLength) {
    var counter = document.getElementById(counterId);
    var currentLength = input.value.length;
    counter.textContent = currentLength + '/' + maxLength;
}

// projectName 및 projectOneLineIntroduction 입력 필드에 대한 이벤트 리스너 추가
var projectNameInput = document.getElementById("projectName");
projectNameInput.addEventListener("input", function () {
    updateTextCounter(this, 'projectNameCounter', 20); // 20은 최대 글자 수입니다.
});

var oneLineIntroductionInput = document.getElementById("projectOneLineIntroduction");
oneLineIntroductionInput.addEventListener("input", function () {
    updateTextCounter(this, 'projectOneLineIntroductionCounter', 50); // 50은 최대 글자 수입니다.
});