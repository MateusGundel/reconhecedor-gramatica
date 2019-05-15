var app = angular.module('myApp', []);
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

app.controller('myCtrl', function ($scope, $http) {
    var debug = true;
    if(debug){
        //inspeciona o elemento ali e depois no console da um $($0).scope().debug = true
        $scope.gramaticaTerminal = "S, A, B";
        $scope.gramaticaNaoTerminal = "c, a, b";
        $scope.gramaticaInicial = "S";
        $scope.listItem = [{id: 0, esquerda: 'S', direita: 'Sa'}];
    }else{
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

    $scope.generate = function () {
        $.blockUI({ message: '<h1><img src="https://scontent.fpoa8-1.fna.fbcdn.net/v/t1.0-9/29315270_1782513481769521_4325627701726543872_n.jpg?_nc_cat=107&_nc_ht=scontent.fpoa8-1.fna&oh=f80982f84264cbf42099379008f0d002&oe=5D5109C6" /> Just a moment...</h1>' });

        $http({
            method: "POST",
            url: '/create_post/',
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
                $scope.finalResult = response;
                $scope.isFinalResult = true;
                $.unblockUI();
            }, function errorCallback(response) {
                console.log(response);
                $.unblockUI();
            });
    }

});