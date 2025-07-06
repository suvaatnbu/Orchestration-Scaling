/*
 * DO NOT EDIT.  THIS FILE IS GENERATED FROM /mnt/tinderbox/7.1-sdk/src/libs/xpcom18a4/xpcom/ds/nsIHashable.idl
 */

#ifndef __gen_nsIHashable_h__
#define __gen_nsIHashable_h__


#ifndef __gen_nsISupports_h__
#include "nsISupports.h"
#endif

/* For IDL files that don't want to include root IDL files. */
#ifndef NS_NO_VTABLE
#define NS_NO_VTABLE
#endif

/* starting interface:    nsIHashable */
#define NS_IHASHABLE_IID_STR "17e595fa-b57a-4933-bd0f-b1812e8ab188"

#define NS_IHASHABLE_IID \
  {0x17e595fa, 0xb57a, 0x4933, \
    { 0xbd, 0x0f, 0xb1, 0x81, 0x2e, 0x8a, 0xb1, 0x88 }}

class NS_NO_VTABLE nsIHashable : public nsISupports {
 public: 

  NS_DEFINE_STATIC_IID_ACCESSOR(NS_IHASHABLE_IID)

  /* boolean equals (in nsIHashable aOther); */
  NS_IMETHOD Equals(nsIHashable * aOther, PRBool *_retval) = 0;

  /* readonly attribute unsigned long hashCode; */
  NS_IMETHOD GetHashCode(PRUint32 *aHashCode) = 0;

};

/* Use this macro when declaring classes that implement this interface. */
#define NS_DECL_NSIHASHABLE \
  NS_IMETHOD Equals(nsIHashable * aOther, PRBool *_retval) NS_OVERRIDE; \
  NS_IMETHOD GetHashCode(PRUint32 *aHashCode) NS_OVERRIDE; 

/* Use this macro to declare functions that forward the behavior of this interface to another object. */
#define NS_FORWARD_NSIHASHABLE(_to) \
  NS_IMETHOD Equals(nsIHashable * aOther, PRBool *_retval) { return _to Equals(aOther, PRBool *_retval); } \
  NS_IMETHOD GetHashCode(PRUint32 *aHashCode) { return _to GetHashCode(aHashCode); } 

/* Use this macro to declare functions that forward the behavior of this interface to another object in a safe way. */
#define NS_FORWARD_SAFE_NSIHASHABLE(_to) \
  NS_IMETHOD Equals(nsIHashable * aOther, PRBool *_retval) { return !_to ? NS_ERROR_NULL_POINTER : _to->Equals(aOther, PRBool *_retval); } \
  NS_IMETHOD GetHashCode(PRUint32 *aHashCode) { return !_to ? NS_ERROR_NULL_POINTER : _to->GetHashCode(aHashCode); } 


#endif /* __gen_nsIHashable_h__ */
