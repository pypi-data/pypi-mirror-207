'use strict';

// the module should depend on 'core' to use the stock services & components
angular.module('ajenti.iptables', ['core']);


'use strict';

angular.module('ajenti.iptables').config(function ($routeProvider) {
    $routeProvider.when('/view/iptables', {
        templateUrl: '/iptables:resources/partial/index.html',
        controller: 'IptablesIndexController'
    });
});


'use strict';

angular.module('ajenti.iptables').controller('IptablesIndexController', function ($scope, $http, pageTitle, gettext, notify, messagebox) {
    pageTitle.set(gettext('Iptables'));

    $scope.paging = {
        'page': 1
    };

    $http.get('/api/iptables/which').then(function () {
        $scope.load();
        $scope.installed = true;
    }, function (err) {
        $scope.ready = true;
        $scope.installed = false;
    });

    $scope.load = function (chain) {
        $http.get('/api/iptables').then(function (resp) {
            $scope.chains = resp.data;
            $scope.chains_list = Object.keys(resp.data);
            if ($scope.chains_list.length > 0) {
                if ($scope.chains_list.indexOf(chain) > 0) {
                    $scope.chains.active_chain = chain;
                } else {
                    $scope.chains.active_chain = $scope.chains_list[0];
                }
                $scope.rules = $scope.chains[$scope.chains.active_chain];
            } else {
                $scope.chains.active_chain = '';
            }
        });
    };

    $scope.update_rules = function () {
        $scope.rules = $scope.chains[$scope.chains.active_chain];
    };

    $scope.delete = function (rule) {
        messagebox.show({
            text: gettext('Really delete the rule ' + rule.rule_line + '?'),
            positive: gettext('Delete'),
            negative: gettext('Cancel')
        }).then(function () {
            $http.delete('/api/iptables/' + $scope.chains.active_chain + '/' + rule.number).then(function (resp) {
                type = resp.data.type;
                msg = resp.data.msg;
                chain = $scope.chains.active_chain;
                if (type == 'success') {
                    notify.success(msg);
                    $scope.load(chain);
                } else {
                    notify.error(msg);
                }
            });
        });
    };
});


