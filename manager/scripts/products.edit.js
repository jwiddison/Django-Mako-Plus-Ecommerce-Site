$(document).ready(function(){
  console.log('page load');
	$('#id_product_type').change(function(){
		if($(this).val() =='RentalProduct')
		{
			$('#id_status').parent().parent().show();
			$('#id_purchase_date').parent().parent().show();
		}
		else
		{
			$('#id_status').parent().parent().hide();
			$('#id_purchase_date').parent().parent().hide();
		}
		if($(this).val() =='IndividualProduct')
		{
			$('#id_create_date').parent().parent().show();
			$('#id_creator').parent().parent().show();
		}
		else
		{
			$('#id_create_date').parent().parent().hide();
			$('#id_creator').parent().parent().hide();
		}
		if($(this).val() =='BulkProduct')
		{
			$('#id_quantity').parent().parent().show();
		}
		else
		{
			$('#id_quantity').parent().parent().hide();
		}
	}); //Change of id field
  $('#id_status').parent().parent().hide();
  $('#id_purchase_date').parent().parent().hide();
  $('#id_create_date').parent().parent().hide();
  $('#id_creator').parent().parent().hide();
  $('#id_quantity').parent().parent().hide();
}); //Document Ready
