function formChaxun(id, f, a, b, c, d) {
    // 2,this,'.qa','.qb'
    // id = 2
    // f = this
    // a = '.qa'
    // b = '.qb'
    // c, d undefined

    // A 是男生星座值
    var A = $(a, f).val(),
    E = ['lnumber'],
    // B 是女生星座值
    B = $(b, f).val(),
    // C undefined
    C = $(c, f).val(),
    // D = 0
    D = $(d, f).size() && $(d, f).attr("checked") == true ? $(d, f).val() : '',
    sQ = 7,
    q = '';
    // 莫名其妙做犀利用的函数
    for (var i = 0; i < E.length; i++) {
        if (id == E[i]) {
            q = A;
            break
        }
    }
    // q 还是空字符，此处为true
    if (!q) {
        // id不是NaN，此处不执行
        // lt = 2
        if (isNaN(id)) lt = id.length;
        else lt = id;
        // 不执行
        // if (lt == 0) lt = 1;
        // lQ = 2
        var lQ = lt % sQ;
        // if (lQ == 0) lQ = 1; // 不执行

        // lA = 男生星座值*2+2
        // sA = lA的字符串长度
        if (A) {
            lA = ((A * (lQ)) + lt);
            sA = lA.toString().length
        } else {
            lA = '';
            sA = 0
        }

        // lB = 女生星座值*2+2
        // sB = lA的字符串长度
        if (B) {
            lB = ((B * (lQ)) + lt);
            sB = lB.toString().length
        } else {
            lB = '';
            sB = 0
        }

        if (C) {
            lC = ((C * (lQ)) + lt);
            sC = lC.toString().length
        } else {
            // 取此处值
            lC = '';
            sC = 0
        }
        if (D) {
            lD = ((D * (lQ)) + lt);
            sD = lD.toString().length
        } else {
            // 取此处值
            lD = '';
            sD = 0
        }
        var q = sA + '' + sB + '' + sC + '' + sD + '' + lA + '' + lB + '' + lC + '' + lD
    }
    $(f).attr("action", "/cx/" + id + "/" + q + ".html");
    $(f).attr("method", "get");
    return true
}
