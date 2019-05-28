from django.shortcuts import render,redirect
from django.contrib import messages,auth
from .models import Contact
from django.core.mail import send_mail


def contact(request):

    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if the user has already made an enquiry 
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id = user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this property')
                return redirect('/listings/'+listing_id)

        #Pass contact values from the enquiry submission form
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contact.save()  # save to database

        #Send email
        '''
        send_mail(
            'Porperty Inquiry',
            'There has been an inquiry for'+ listing + ' . ',
            'sydneybleuops@gmail.com',
            ['sydneybleuops@gmail.com'],
            fail_silently=False,
        )
        '''
        
        messages.success(request,'You request has been submitted, an agent will come back to you the soonest')

        return redirect('/listings/'+listing_id)