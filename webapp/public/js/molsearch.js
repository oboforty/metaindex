
let jsmeApplet;

export function init_jsme(el) {

    window.jsmeOnLoad = function() {
        //this function will be called after the JavaScriptApplet code has been loaded.
        jsmeApplet = new JSApplet.JSME("jsme_container", "420px", "420px", {
            "options": "oldlook,marker,markermenu",
            "atombgsize": "0.5",
            "bondbgsize": "0.2",
            "guicolor": "#e9ecef",
        });
        window.jsme = jsmeApplet;
        console.log("JSME initialized!");

        // forward callbacks to vue component:
        //jsmeApplet.setAfterStructureModifiedCallback(el.onEdit);
        //jsmeApplet.getAlldefinedCallBackNames()

        //jsmeApplet.setCallBack("AfterStructureModified", el.onEdit);
        el.jsme = jsmeApplet;
        el.jsme_mol2inchi = computeInchi;
    }
}


function computeInchi(mol) {
    var result;
    var tmp_function_name = "__local_ff";
    JSApplet.Inchi[tmp_function_name] = function (inchi_result) {
        result = inchi_result
    };
    JSApplet.Inchi.computeInchi(mol, "JSApplet.Inchi." + tmp_function_name);
    delete JSApplet.Inchi[tmp_function_name];

    return result;
}
