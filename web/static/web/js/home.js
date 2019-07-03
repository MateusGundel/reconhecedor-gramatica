var app = angular.module('myApp', []);
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

app.controller('myCtrl', function ($scope, $http) {
    var debug = false;
    if (debug) {
        var objeto_gramatica = gramatica_exemplo(2);
        //inspeciona o elemento ali e depois no console da um $($0).scope().debug = true
        $scope.gramaticaTerminal = objeto_gramatica.gramaticaTerminal;
        $scope.gramaticaNaoTerminal = objeto_gramatica.gramaticaNaoTerminal;
        $scope.gramaticaInicial = objeto_gramatica.gramaticaInicial;
        $scope.listItem = objeto_gramatica.listItem;
    } else {
        $scope.gramaticaTerminal = "";
        $scope.gramaticaNaoTerminal = "";
        $scope.gramaticaInicial = "";
        $scope.listItem = [{id: 0, esquerda: '', direita: ''}];
    }
    $scope.finalResult = "";
    $scope.isFinalResult = false;
    $scope.addItem = function () {
        $scope.listItem.push({id: $scope.listItem[$scope.listItem.length - 1]['id'] + 1, esquerda: '', direita: ''});
        console.log($scope.listItem)
    }

    $scope.removeItem = function (id) {
        if ($scope.listItem.length > 1) {
            $scope.listItem.forEach(function (element, index) {
                if (element['id'] === id) {
                    console.log(index);
                    console.log(element['id']);
                    $scope.listItem.splice(index, 1)
                    console.log($scope.listItem)
                }
            });
        }
    }

    $scope.generate = function (tipo) {
        // $.blockUI({ message: '<h1><img src="https://scontent.fpoa8-1.fna.fbcdn.net/v/t1.0-9/29315270_1782513481769521_4325627701726543872_n.jpg?_nc_cat=107&_nc_ht=scontent.fpoa8-1.fna&oh=f80982f84264cbf42099379008f0d002&oe=5D5109C6" /> Just a moment...</h1>' });
        $.blockUI({message: 'Please Wait'});
        switch (tipo) {
            case 1:
                verificarGramatica();
            case 2:
                transformarGlc();
        }
        $.unblockUI();

    }

    transformarGlc = function () {
        $http({
            method: "POST",
            url: '/transformar/',
            data: {
                'gramatica-terminal': $scope.gramaticaTerminal,
                'gramatica-nao-terminal': $scope.gramaticaNaoTerminal,
                'gramatica-inicial': $scope.gramaticaInicial,
                'producao': $scope.listItem
            },
            headers: {
                'Content-Type': undefined
            }
        })
            .then(function successCallback(response) {
                $scope.finalResult = JSON.parse(JSON.stringify(response.data));
                console.log($scope.finalResult.sentencas)
                $scope.isFinalResult = true;
            }, function errorCallback(response) {
                console.log(response);
            });
    }

    verificarGramatica = function () {
        $http({
            method: "POST",
            url: '/reconhecer/',
            data: {
                'gramatica-terminal': $scope.gramaticaTerminal,
                'gramatica-nao-terminal': $scope.gramaticaNaoTerminal,
                'gramatica-inicial': $scope.gramaticaInicial,
                'producao': $scope.listItem
            },
            headers: {
                'Content-Type': undefined
            }
        })
            .then(function successCallback(response) {
                $scope.finalResult = JSON.parse(JSON.stringify(response.data));
                console.log($scope.finalResult.sentencas)
                $scope.isFinalResult = true;
            }, function errorCallback(response) {
                console.log(response);
            });
    }
});


gramatica_exemplo = function (tipo_gramatica) {
    var objeto_gramatica = {};
    switch (tipo_gramatica) {
        case 0:
            objeto_gramatica = {
                "gramaticaNaoTerminal": "A, B, C",
                "gramaticaTerminal": "a, b",
                "gramaticaInicial": "A",
                "L(G)": "ba, ab",
                "listItem": [
                    {
                        id: 0,
                        esquerda: "A",
                        direita: "BC"
                    },
                    {
                        id: 1,
                        esquerda: "C",
                        direita: "CB"
                    },
                    {
                        id: 2,
                        esquerda: "B",
                        direita: "b"
                    },
                    {
                        id: 3,
                        esquerda: "C",
                        direita: "a"
                    }
                ]
            }
            break;
        case 1:
            objeto_gramatica = {
                "gramaticaNaoTerminal": "S, B, C",
                "gramaticaTerminal": "a, b, c",
                "gramaticaInicial": "S",
                "L(G)": "anbncn | n>=1}",
                "listItem": [
                    {
                        id: 0,
                        esquerda: "S",
                        direita: "aSBC"
                    },
                    {
                        id: 2,
                        esquerda: "S",
                        direita: "aBC"
                    },
                    {
                        id: 3,
                        esquerda: "B",
                        direita: "BC"
                    },
                    {
                        id: 4,
                        esquerda: "B",
                        direita: "ab"
                    },
                    {
                        id: 5,
                        esquerda: "B",
                        direita: "bb"
                    },
                    {
                        id: 6,
                        esquerda: "C",
                        direita: "bc"
                    },
                    {
                        id: 7,
                        esquerda: "C",
                        direita: "cc"
                    }
                ]
            }
            break;
        case 2:
            console.warn("Não há nenhuma gramática do tipo GLC cadastrada");
            objeto_gramatica = {
                "gramaticaNaoTerminal": "A, B, C",
                "gramaticaTerminal": "a, b",
                "gramaticaInicial": "A",
                "L(G)": "ba, ab",
                "listItem": [
                    {
                        id: 0,
                        esquerda: "A",
                        direita: "BC"
                    },
                    {
                        id: 0,
                        esquerda: "C",
                        direita: "CB"
                    },
                    {
                        id: 0,
                        esquerda: "B",
                        direita: "b"
                    },
                    {
                        id: 0,
                        esquerda: "C",
                        direita: "a"
                    }
                ]
            }
            break;
        case 3:
            objeto_gramatica = objeto_gramatica = {
                "gramaticaNaoTerminal": "S",
                "gramaticaTerminal": "a, b",
                "gramaticaInicial": "S",
                "L(G)": "{anb; n ≥0} ou a*b",
                "listItem": [
                    {
                        id: 0,
                        esquerda: "S",
                        direita: "aS"
                    },
                    {
                        id: 1,
                        esquerda: "S",
                        direita: "b"
                    }
                ]
            }
            break;
        default:
            console.error("tipo de gramática inválido");
            break;
    }
    ;
    console.log(objeto_gramatica);
    return objeto_gramatica;
};

