var phonecatApp = angular.module('fineline', []);

/* this is bad practice, but whatever......we're just hacking something toegether here anyways */
var getClientToken = function(scope) {
  $.ajax({
    type: "GET",
    url: "/api-payments/clienttoken",
    success: function(data) {
      scope.clientToken = data.token;
    }
  });
};

var postOrder = function(scope, nonce) {
  debugger;
  var address = scope.roomNumber + ", " + scope.bldgName;
  var listSku = [];
  
  for (var i = 0; i < scope.items.length; i++) {
    listSku.push(scope.items[i].sku);
    listSku.push(scope.items[i].count);
  }
  
  $.ajax({
    type: "POST",
    url: "/api-orders/placeorder/",
    data: {"address": address, "name": scope.name, "datetime": scope.time, "payment_nonce": nonce, "sku": listSku},
    success: function(data) {
      // do nothing really....
    },
  }).fail(function() {
    alert("A processing error occured! Please try placing your order again!");
  })
}



phonecatApp.controller('browseItemController', function ($scope) {
  
  var BROWSE_STATE = 0;
  var CONFIRM_STATE = 1;
  var DELIVERY_STATE = 2;
  var PAYMENT_STATE = 3;
  var THANK_STATE = 4;
  
  
  $scope.items = globalItems;
  $scope.purchaseState = BROWSE_STATE; // initial browse state. S1 = the confirm stage, s2 = the delivery state, s3 = payment state, s4 = thank you!
  $scope.buttonsActive = false;
  $scope.orderCost = 0;
  $scope.braintree; // used to initiate the braintree element later on.
  $scope.time = "";
  $scope.bldgName = "";
  $scope.roomNumber = "";
  $scope.name == "";
  $scope.clientToken = "";
  
  
  $scope.addToCart = function(item) {
    item.count = item.count + 1;
    $scope.calculateOrderTotal();
  };
  
  $scope.removeFromCart = function(item) {
    if (item.count > 0) {
      item.count = item.count - 1;
      $scope.calculateOrderTotal();
    }
  }
  
  $scope.backToBeginning = function() {
    $scope.items = globalItems;
    $scope.purchaseState = BROWSE_STATE;
  }
  
  $scope.submitOrder = function() {
    $scope.purchaseState = THANK_STATE;
  }
  
  $scope.calculateOrderTotal = function() {
    $scope.orderCost = 0;
    for (var i = 0; i < $scope.items.length; i++) {
      $scope.orderCost += parseFloat($scope.items[i].price) * parseFloat($scope.items[i].count);
    }
  };
  
  $scope.nextPaymentStep = function() {
    // this function deals with hiding all zero count entries in the table.
    $scope.tmp = $scope.items.slice(0);
    $scope.new = [];
    // $scope.buttonsActive = true;
    switch($scope.purchaseState) {
      
      case BROWSE_STATE:
        getClientToken($scope);
        
        for (var i = 0; i < $scope.items.length; i++) {
          if ($scope.items[i].count !== 0) {
            $scope.new.push($scope.items[i]);
          }
        }
    
        $scope.items = $scope.new;
        
        // calculate the order total
        $scope.calculateOrderTotal();
        
        $scope.purchaseState = CONFIRM_STATE;
        break;
        
      case CONFIRM_STATE:
        $scope.purchaseState = DELIVERY_STATE;
        // no other processing needs to be done at this stage.
        break;
      case DELIVERY_STATE:
        // in this state we first need to check that all reqiured fields were filled out, else reject advancement.
        if ($("#name").val() != "" && $("#dormrm").val() != "" && $("#bldg").val() != "" && $("#time").val() != "") {
          // we are good to go.
          // time to move to the braintree screen!
          $scope.name = $("#name").val();
          $scope.roomNumber = $("#dormrm").val();
          $scope.bldgName = $("#bldg").val();
          $scope.time = $("#time").val();
          $scope.purchaseState = PAYMENT_STATE;
          if ($scope.braintree === undefined || $scope.braintree === null) {
            var myScope = $scope;
            $scope.braintree = braintree.setup($scope.clientToken, 'dropin', {
                              container: 'dropin',
                              paymentMethodNonceReceived: function(event, nonce) {
                                postOrder(myScope, nonce);
                              }
                             });            
          }
        } else {
          alert("A form error occured. Please try again!");
        }
        
        break;
    }  
  }
  
  $scope.previousPaymentStep = function() {
    switch($scope.purchaseState) {
      case CONFIRM_STATE:
        // we want to make sure that in this state we put back the tmp that exists when the back is pressed
        $scope.items = globalItems;
        break;
      case DELIVERY_STATE:
        break; // there is nothing that needs to be done when back is pressed at this state.
      case PAYMENT_STATE:
        $("#dropin").empty();
    }
    
    $scope.purchaseState = $scope.purchaseState - 1;
  }
});