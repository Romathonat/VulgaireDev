function isInt(n) {
    return Number(n) === n && n % 1 === 0;
}

function deepCopy(arraySource) {
    var arrayCible = [];
    for (var i = 0; i < arraySource.length; i++) {
        arrayCible.push(arraySource[i]);
    }
    return arrayCible;
}
function calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche) {

    //on test si on a trouvé le bon nombre
    for (var i = 0; i < nombres.length; i++) {
        if (nombres[i] == aim) {
            solutions.push(deepCopy(solutionCourante));
            return;
        }
        //si jamais on arrive pas à la solution, on garde la solution la plus proche qu'on ai trouvé
        if (Math.abs(aim - nombres[i]) < Math.abs(aim - solutionPlusProche[0])) {
            //on remplace l'ancienne valeur
            while (solutionPlusProche.length > 0) {
                solutionPlusProche.pop();
            }

            solutionPlusProche.push(nombres[i]);
            solutionPlusProche.push(deepCopy(solutionCourante));
        }
    }

    //si on arrive à un seul nombre (et qu'il n'est pas aim), on termine
    if (nombres.length == 1) {
        return;
    }

    //pour tous les nombres disponibles, on liste toutes les façons d'en prendre 2
    for (var i = 0; i < nombres.length; i++) {
        if (nombres[i] > 0) {
            for (var j = 0; j < i; j++) {
                if (nombres[j] > 0) {

                    var nombre1 = Math.round(nombres[i]);
                    var nombre2 = Math.round(nombres[j]);

                    //on invalide ces deux nombres de la liste en les mettant négatifs
                    nombres[i] = -nombres[i];
                    nombres[j] = -nombres[j];

                    //on lance la récurence pour les 4 opérations possibles
                    nombres.push(nombre1 + nombre2);
                    solutionCourante.push((nombre1.toString()) +
                        "+" + (nombre2.toString()) + "=" + (nombre1 + nombre2).toString()
                    )
                    ;
                    calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche);
                    solutionCourante.pop();
                    nombres.pop();

                    nombres.push(nombre1 - nombre2);
                    solutionCourante.push(nombre1.toString() +
                        "-" + nombre2.toString() + "=" + (nombre1 - nombre2).toString()
                    )
                    ;
                    calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche);
                    solutionCourante.pop();
                    nombres.pop();

                    nombres.push(nombre1 * nombre2);
                    solutionCourante.push(nombre1.toString() +
                        "*" + nombre2.toString() + "=" + (nombre1 * nombre2).toString()
                    );
                    calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche);
                    solutionCourante.pop();
                    nombres.pop();

                    //on ne fait le résultat que si la division est un entier
                    resultatDivision = Math.max(nombre1, nombre2) / Math.min(nombre1, nombre2);
                    if (isInt(resultatDivision)) {
                        nombres.push(resultatDivision);
                        solutionCourante.push(Math.max(nombre1, nombre2).toString() + "/" + Math.min(nombre1, nombre2).toString() + "=" + resultatDivision.toString());
                        calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche);
                        solutionCourante.pop();
                        nombres.pop();
                    }

                    //on réactive ces nombres maintenant qu'on a fini de travailler avec eux
                    nombres[i] = -nombres[i];
                    nombres[j] = -nombres[j];
                }
            }
        }
    }
}

function calculerSolution() {
    document.getElementById("titreSolution").innerHTML = "Calcul en cours...";
    var nombres = [];

    for (var i = 0; i < 6; i++) {
        nombres.push(document.getElementById("lesChiffresNombre" + (i + 1)).value);
    }

    aim = document.getElementById("aim").value;

    solutionPlusProche = [0, []];
    solutions = [];
    solutionCourante = [];

    calculRec(nombres, aim, solutionCourante, solutions, solutionPlusProche);

    var solution = solutions[0];
    var texteTitre = "";
    if (solutions.length === 0) {
        solution = solutionPlusProche[1];
        texteTitre = "Solution la plus proche trouvée:"
    }
    else{
        texteTitre = "Solution la plus proche trouvée:"
    }

    document.getElementById("titreSolution").innerHTML = texteTitre;
    document.getElementById("solution").innerHTML = solution.join("</br>");
}
