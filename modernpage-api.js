function mordenpageToJS(code) {
    code = code.replace(/\$var/g, 'let');  
    code = code.replace(/\$echo/g, 'document.write'); 
    code = code.replace(/\$if/g, 'if');  
    code = code.replace(/\$for/g, 'for');  
    code = code.replace(/\$while/g, 'while');  
    code = code.replace(/\$readFile\((.*?)\)/g, 'await $readFile($1)');  

    return code;
}

async function $readFile(filePath) {
    const response = await fetch('/readfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ file_path: filePath })
    });
    const data = await response.json();
    if (data.error) {
        console.error(data.error);
        return "Error reading file";
    }
    return data.content;
}

document.querySelectorAll("mordenpage").forEach(async tag => {
    let jsCode = mordenpageToJS(tag.innerHTML);
    eval(await jsCode); 
});