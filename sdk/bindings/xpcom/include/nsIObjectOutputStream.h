/*
 * DO NOT EDIT.  THIS FILE IS GENERATED FROM /mnt/tinderbox/7.1-sdk/src/libs/xpcom18a4/xpcom/io/nsIObjectOutputStream.idl
 */

#ifndef __gen_nsIObjectOutputStream_h__
#define __gen_nsIObjectOutputStream_h__


#ifndef __gen_nsIBinaryOutputStream_h__
#include "nsIBinaryOutputStream.h"
#endif

/* For IDL files that don't want to include root IDL files. */
#ifndef NS_NO_VTABLE
#define NS_NO_VTABLE
#endif

/* starting interface:    nsIObjectOutputStream */
#define NS_IOBJECTOUTPUTSTREAM_IID_STR "92c898ac-5fde-4b99-87b3-5d486422094b"

#define NS_IOBJECTOUTPUTSTREAM_IID \
  {0x92c898ac, 0x5fde, 0x4b99, \
    { 0x87, 0xb3, 0x5d, 0x48, 0x64, 0x22, 0x09, 0x4b }}

class NS_NO_VTABLE nsIObjectOutputStream : public nsIBinaryOutputStream {
 public: 

  NS_DEFINE_STATIC_IID_ACCESSOR(NS_IOBJECTOUTPUTSTREAM_IID)

  /* void writeObject (in nsISupports aObject, in PRBool aIsStrongRef); */
  NS_IMETHOD WriteObject(nsISupports * aObject, PRBool aIsStrongRef) = 0;

  /* void writeSingleRefObject (in nsISupports aObject); */
  NS_IMETHOD WriteSingleRefObject(nsISupports * aObject) = 0;

  /* void writeCompoundObject (in nsISupports aObject, in nsIIDRef aIID, in PRBool aIsStrongRef); */
  NS_IMETHOD WriteCompoundObject(nsISupports * aObject, const nsIID & aIID, PRBool aIsStrongRef) = 0;

  /* void writeID (in nsIDRef aID); */
  NS_IMETHOD WriteID(const nsID & aID) = 0;

  /* [notxpcom] charPtr getBuffer (in PRUint32 aLength, in PRUint32 aAlignMask); */
  NS_IMETHOD_(char *) GetBuffer(PRUint32 aLength, PRUint32 aAlignMask) = 0;

  /* [notxpcom] void putBuffer (in charPtr aBuffer, in PRUint32 aLength); */
  NS_IMETHOD_(void) PutBuffer(char * aBuffer, PRUint32 aLength) = 0;

};

/* Use this macro when declaring classes that implement this interface. */
#define NS_DECL_NSIOBJECTOUTPUTSTREAM \
  NS_IMETHOD WriteObject(nsISupports * aObject, PRBool aIsStrongRef) NS_OVERRIDE; \
  NS_IMETHOD WriteSingleRefObject(nsISupports * aObject) NS_OVERRIDE; \
  NS_IMETHOD WriteCompoundObject(nsISupports * aObject, const nsIID & aIID, PRBool aIsStrongRef) NS_OVERRIDE; \
  NS_IMETHOD WriteID(const nsID & aID) NS_OVERRIDE; \
  NS_IMETHOD_(char *) GetBuffer(PRUint32 aLength, PRUint32 aAlignMask) NS_OVERRIDE; \
  NS_IMETHOD_(void) PutBuffer(char * aBuffer, PRUint32 aLength) NS_OVERRIDE; 

/* Use this macro to declare functions that forward the behavior of this interface to another object. */
#define NS_FORWARD_NSIOBJECTOUTPUTSTREAM(_to) \
  NS_IMETHOD WriteObject(nsISupports * aObject, PRBool aIsStrongRef) { return _to WriteObject(aObject, aIsStrongRef); } \
  NS_IMETHOD WriteSingleRefObject(nsISupports * aObject) { return _to WriteSingleRefObject(aObject); } \
  NS_IMETHOD WriteCompoundObject(nsISupports * aObject, const nsIID & aIID, PRBool aIsStrongRef) { return _to WriteCompoundObject(aObject, aIID, aIsStrongRef); } \
  NS_IMETHOD WriteID(const nsID & aID) { return _to WriteID(aID); } \
  NS_IMETHOD_(char *) GetBuffer(PRUint32 aLength, PRUint32 aAlignMask) { return _to GetBuffer(aLength, aAlignMask); } \
  NS_IMETHOD_(void) PutBuffer(char * aBuffer, PRUint32 aLength) { return _to PutBuffer(aBuffer, aLength); } 

/* Use this macro to declare functions that forward the behavior of this interface to another object in a safe way. */
#define NS_FORWARD_SAFE_NSIOBJECTOUTPUTSTREAM(_to) \
  NS_IMETHOD WriteObject(nsISupports * aObject, PRBool aIsStrongRef) { return !_to ? NS_ERROR_NULL_POINTER : _to->WriteObject(aObject, aIsStrongRef); } \
  NS_IMETHOD WriteSingleRefObject(nsISupports * aObject) { return !_to ? NS_ERROR_NULL_POINTER : _to->WriteSingleRefObject(aObject); } \
  NS_IMETHOD WriteCompoundObject(nsISupports * aObject, const nsIID & aIID, PRBool aIsStrongRef) { return !_to ? NS_ERROR_NULL_POINTER : _to->WriteCompoundObject(aObject, aIID, aIsStrongRef); } \
  NS_IMETHOD WriteID(const nsID & aID) { return !_to ? NS_ERROR_NULL_POINTER : _to->WriteID(aID); } \
  NS_IMETHOD_(char *) GetBuffer(PRUint32 aLength, PRUint32 aAlignMask) { return !_to ? NS_ERROR_NULL_POINTER : _to->GetBuffer(aLength, aAlignMask); } \
  NS_IMETHOD_(void) PutBuffer(char * aBuffer, PRUint32 aLength) { return !_to ? NS_ERROR_NULL_POINTER : _to->PutBuffer(aBuffer, aLength); } 



inline nsresult
NS_WriteOptionalObject(nsIObjectOutputStream* aStream, nsISupports* aObject,
                       PRBool aIsStrongRef)
{
    PRBool nonnull = (aObject != nsnull);
    nsresult rv = aStream->WriteBoolean(nonnull);
    if (NS_SUCCEEDED(rv) && nonnull)
        rv = aStream->WriteObject(aObject, aIsStrongRef);
    return rv;
}

inline nsresult
NS_WriteOptionalSingleRefObject(nsIObjectOutputStream* aStream,
                                nsISupports* aObject)
{
    PRBool nonnull = (aObject != nsnull);
    nsresult rv = aStream->WriteBoolean(nonnull);
    if (NS_SUCCEEDED(rv) && nonnull)
        rv = aStream->WriteSingleRefObject(aObject);
    return rv;
}

inline nsresult
NS_WriteOptionalCompoundObject(nsIObjectOutputStream* aStream,
                               nsISupports* aObject,
                               const nsIID& aIID,
                               PRBool aIsStrongRef)
{
    PRBool nonnull = (aObject != nsnull);
    nsresult rv = aStream->WriteBoolean(nonnull);
    if (NS_SUCCEEDED(rv) && nonnull)
        rv = aStream->WriteCompoundObject(aObject, aIID, aIsStrongRef);
    return rv;
}


#endif /* __gen_nsIObjectOutputStream_h__ */
