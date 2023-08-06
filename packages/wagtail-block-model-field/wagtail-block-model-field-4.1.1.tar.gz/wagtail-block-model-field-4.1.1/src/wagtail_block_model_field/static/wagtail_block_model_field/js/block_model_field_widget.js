
function initBlockModelWidget(id) {

    const body = document.querySelector('#' + id + '[data-block]');

    const blockDefData = JSON.parse(body.dataset.block);
    const blockDef = window.telepath.unpack(blockDefData);
    const blockValue = JSON.parse(body.dataset.value);
    const blockErrors = window.telepath.unpack(JSON.parse(body.dataset.errors));

    const blockInstance = blockDef.render(body, id, blockValue, null);

    if( blockErrors != null) {
        if( blockErrors.length != undefined && blockErrors.length != 0 ) {
            blockInstance.setError(blockErrors);
        }
    }
}

window.initBlockModelWidget = initBlockModelWidget;
