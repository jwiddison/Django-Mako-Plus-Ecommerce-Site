$(document).ready(function(){
		if($('#pType_saved').attr('data-pType') =='Rental Product')
		{
			$('#id_status').parent().parent().show();
			$('#id_purchase_date').parent().parent().show();
		}
		else
		{
			$('#id_status').parent().parent().hide();
			$('#id_purchase_date').parent().parent().hide();
		}
		if($('#pType_saved').attr('data-pType') =='Individual Product')
		{
			$('#id_create_date').parent().parent().show();
			$('#id_creator').parent().parent().show();
		}
		else
		{
			$('#id_create_date').parent().parent().hide();
			$('#id_creator').parent().parent().hide();
		}
		if($('#pType_saved').attr('data-pType') =='Bulk Product')
		{
			$('#id_quantity').parent().parent().show();
		}
		else
		{
			$('#id_quantity').parent().parent().hide();
		}
}); //Document Ready
