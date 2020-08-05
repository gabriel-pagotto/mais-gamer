function init() {
    render()
    enableEditMode();
};

function enableEditMode() {
    const textField = document.querySelector('.text-field');
    textField.contentDocument.designMode = 'On';
};

function actions(command, arg = null) {
    const textField = document.querySelector('.text-field');
    document.querySelector('.text-field').focus()
    textField.contentDocument.execCommand(command, false, arg);
    document.querySelector('.text-field').focus()
};

$(function () {
    $('#image-upload-file-input').change(function () {
        const textField = document.querySelector('.text-field');
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        fileReader.readAsDataURL(file);
        fileReader.onloadend = function () {
            textField.contentDocument.execCommand('insertImage', true, fileReader.result);
            $('.text-field').focus();
        }
    });
});

function addDataOnTextArea(value) {
    console.log('OKay')
};


function render() {
    const editor = document.querySelector('.editor')

    editor.innerHTML = `

    <div class="editor-header">
        <input class="ps-absolute o0" type="file" name="file" accept="image/*" id="image-upload-file-input" style="display:none;">
        <label id="undo"><i onclick="actions('undo')" class="fa fa-undo"></i></label>
        <label id="redo"><i onclick="actions('redo')" class="fa fa-repeat"></i></label>
        <label id="bold"><i onclick="actions('bold')" class="fa fa-bold"></i></label>
        <label for="image-upload-file-input" id="insertImage"><i class="fa fa-image"></i></label>
        <label id="createLink"><i onclick="actions('createLink', prompt('Coloque o link aqui', 'https://'))" class="fa fa-link"></i></label>
        <label id="unlink"><i onclick="actions('unlink')" class="fa fa-unlink"></i></label>
        <label id="insertUnorderedList"><i onclick="actions('insertUnorderedList')" class="fas fa-list-ul"></i></label>
        <label id="cut"><i onclick="actions('cut')" class="fas fa-cut"></i></label>
        <label id="copy"><i onclick="actions('copy')" class="fas fa-copy"></i></label>
        <label id="paste"><i onclick="actions('paste')" class="fas fa-paste"></i></label>
        <label id="delete"><i onclick="actions('delete')" class="fa fa-trash-alt"></i></label>
    </div>
    <iframe name="text-field" class="text-field" frameborder="0" onchange="addDataOnTextArea()"></iframe>
    `
};

init()
