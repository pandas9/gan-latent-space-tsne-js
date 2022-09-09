const getPersisentObject = (objectName) => {
    let sessionObject = undefined;
    
    for (const el of document.cookie.split(';')) {
        const cookie_value = el.split('=');
        if (cookie_value[0].trim() === objectName) {
            sessionObject = cookie_value[1];
            break;
        }
    }

    return sessionObject;
};

const setPersisentObject = (object, objectName, session=true) => {
    if (session) {
        document.cookie = `${objectName}=${object}; SameSite=Lax; path=/;`;
    } else {
        document.cookie = `${objectName}=${object}; SameSite=Lax; path=/; max-age=31536000;`;
    }
};

const selectConfig = (e) => {
    setPersisentObject(e.value, 'config');
    window.location.reload();
};
