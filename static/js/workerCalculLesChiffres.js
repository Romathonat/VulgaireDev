

//on definit ce que ce worker doit faire
self.addEventListener('message', receiveMessage);

function receiveMessage(e) {
    calculRec(e.data.nombres, e.data.aim, e.data.solutionCourante, e.data.solutions, e.data.solutionPlusProche);
    self.postMessage({solutions : JSON.stringify(e.data.nombres), solutionPlusProche : JSON.stringify(e.data.solutionPlusProche) });
}
