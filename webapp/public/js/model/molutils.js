

export function colorize_moltext(text) {
    const coloring = {
        'C': '<b class="text-dark">{$}</b>',
        'O': '<b class="text-danger">{$}</b>',
        'N': '<b class="text-info">{$}</b>',
        'P': '<b style="color:orange;">{$}</b>',
        'S': '<b class="text-warning">{$}</b>',
        'Cl': '<b class="text-success">{$}</b>',
        'H': '<b style="color:#939393;">{$}</b>',
        empty: '<i style="">{$}</i>'
    };

    return text.replace(/([A-Z]{1}[a-z]{0,2})(\d*)/gm, function(match, a,b){
        if (coloring[a])
            return coloring[a].replace('{$}', a+b);
        else
            return a+b;
    });
}

// todo: inchi reszekre bont
