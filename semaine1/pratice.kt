fun est_pair(a: Int): Boolean {
    if (a % 2 == 0) {
        return true
    } else {
        return false
    }
}

fun afficher_pair(nombres: list<Int>) :{
    for (nombre in nombres) {
        if (est_pair(nombre))
        println(nombre)
    }
}