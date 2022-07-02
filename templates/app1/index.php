<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.1.1/css/bootstrap.min.css"/>

</head>
<body class="bg-dark">
       <div class="container">
         <div class="row my-4">
          <div class ="col-lg-10 mx-auto">
            <div class="card-shadow">
               
               <div class="card-body p-4">
                <div id="show_alert"></div>
                  <form action="#" method="POST" id="add_form">
                    <div id="show_item">
                     <div class="row">
                      <div class="col-md-4 mb-3">
                          <input type="text" name="productname[]" class="form-control"
                          placeholder="Select Product"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="sku[]" class="form-control"
                          placeholder="SKU"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="quantity[]" class="form-control"
                          placeholder="Quantity"  required >
                      </div>
                       <div class="col-md-3 mb-3">
                          <input type="number" name="price[]" class="form-control"
                          placeholder="Price"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="amount[]" class="form-control"
                          placeholder="Amount"  required >
                      </div>
                      <div class="col-md-2 mb-3 d-grid">
                        <button class="btn btn-success add_item_button">Add More</button>
                     </div>       
 
                    </div>
                  </div>
                  <div>
                    <input type="submit" value="Add" class="btn btn-primary w-25" id="add_item_btn">
                 </div>    

                </form>
                </div>    
                      
                      








              
           </div>
         </div>
        </div>
</div>
<script src="https://cdnjs.cloudfare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script>
   $(document).ready(function() {
    $(".add_item_btn").click(function(e) {
        e.preventDefault();
        $("#show_item").prepend(`<div class="row">
                      <div class="col-md-4 mb-3">
                          <input type="text" name="productname[]" class="form-control"
                          placeholder="Select Product"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="sku[]" class="form-control"
                          placeholder="SKU"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="quantity[]" class="form-control"
                          placeholder="Quantity"  required >
                      </div>
                       <div class="col-md-3 mb-3">
                          <input type="number" name="price[]" class="form-control"
                          placeholder="Price"  required >
                      </div>
                      <div class="col-md-3 mb-3">
                          <input type="number" name="amount[]" class="form-control"
                          placeholder="Amount"  required >
                      </div>
                      <div class="col-md-2 mb-3 d-grid">
                        <button class="btn btn-danger remove_item_button">Remove</button>
                     </div>       
 
                    </div>

        )`;
    });
$(document).on('click',remove_item_button,function(e){
    e.preventDefault();
    let row_item=$(this).parent().parent();
    $(row_item).remove();
});

$("#add_form").submit(function(e){
    e.preventDefault();
    $("#add_btn").val('Adding....');
    $.ajax({
        url:'action.php'
        method:'post',
        data:$(this).serialize(),
        success:function(response){
            $("#add_btn").val('add');
            $("#add_form")[0].reset();
            $(".append_item").remove(); 
            $("#show_alert").html(`<div class="alert alert-success" role="alert">${response}</div>`);
        }
        

    });

});
});

</script>

</body>
</html>

