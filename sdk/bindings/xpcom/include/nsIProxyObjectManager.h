/*
 * DO NOT EDIT.  THIS FILE IS GENERATED FROM /mnt/tinderbox/7.1-sdk/src/libs/xpcom18a4/xpcom/proxy/public/nsIProxyObjectManager.idl
 */

#ifndef __gen_nsIProxyObjectManager_h__
#define __gen_nsIProxyObjectManager_h__


#ifndef __gen_nsISupports_h__
#include "nsISupports.h"
#endif

/* For IDL files that don't want to include root IDL files. */
#ifndef NS_NO_VTABLE
#define NS_NO_VTABLE
#endif
class nsIEventQueue; /* forward declaration */


/* starting interface:    nsIProxyObjectManager */
#define NS_IPROXYOBJECTMANAGER_IID_STR "eea90d43-b059-11d2-915e-c12b696c9333"

#define NS_IPROXYOBJECTMANAGER_IID \
  {0xeea90d43, 0xb059, 0x11d2, \
    { 0x91, 0x5e, 0xc1, 0x2b, 0x69, 0x6c, 0x93, 0x33 }}

class NS_NO_VTABLE nsIProxyObjectManager : public nsISupports {
 public: 

  NS_DEFINE_STATIC_IID_ACCESSOR(NS_IPROXYOBJECTMANAGER_IID)

  /* void getProxyForObject (in nsIEventQueue destQueue, in nsIIDRef iid, in nsISupports object, in PRInt32 proxyType, [iid_is (iid), retval] out nsQIResult result); */
  NS_IMETHOD GetProxyForObject(nsIEventQueue * destQueue, const nsIID & iid, nsISupports * object, PRInt32 proxyType, void * *result) = 0;

  /* void getProxy (in nsIEventQueue destQueue, in nsIIDRef cid, in nsISupports aOuter, in nsIIDRef iid, in PRInt32 proxyType, [iid_is (iid), retval] out nsQIResult result); */
  NS_IMETHOD GetProxy(nsIEventQueue * destQueue, const nsIID & cid, nsISupports * aOuter, const nsIID & iid, PRInt32 proxyType, void * *result) = 0;

};

/* Use this macro when declaring classes that implement this interface. */
#define NS_DECL_NSIPROXYOBJECTMANAGER \
  NS_IMETHOD GetProxyForObject(nsIEventQueue * destQueue, const nsIID & iid, nsISupports * object, PRInt32 proxyType, void * *result) NS_OVERRIDE; \
  NS_IMETHOD GetProxy(nsIEventQueue * destQueue, const nsIID & cid, nsISupports * aOuter, const nsIID & iid, PRInt32 proxyType, void * *result) NS_OVERRIDE; 

/* Use this macro to declare functions that forward the behavior of this interface to another object. */
#define NS_FORWARD_NSIPROXYOBJECTMANAGER(_to) \
  NS_IMETHOD GetProxyForObject(nsIEventQueue * destQueue, const nsIID & iid, nsISupports * object, PRInt32 proxyType, void * *result) { return _to GetProxyForObject(destQueue, iid, object, proxyType, result); } \
  NS_IMETHOD GetProxy(nsIEventQueue * destQueue, const nsIID & cid, nsISupports * aOuter, const nsIID & iid, PRInt32 proxyType, void * *result) { return _to GetProxy(destQueue, cid, aOuter, iid, proxyType, result); } 

/* Use this macro to declare functions that forward the behavior of this interface to another object in a safe way. */
#define NS_FORWARD_SAFE_NSIPROXYOBJECTMANAGER(_to) \
  NS_IMETHOD GetProxyForObject(nsIEventQueue * destQueue, const nsIID & iid, nsISupports * object, PRInt32 proxyType, void * *result) { return !_to ? NS_ERROR_NULL_POINTER : _to->GetProxyForObject(destQueue, iid, object, proxyType, result); } \
  NS_IMETHOD GetProxy(nsIEventQueue * destQueue, const nsIID & cid, nsISupports * aOuter, const nsIID & iid, PRInt32 proxyType, void * *result) { return !_to ? NS_ERROR_NULL_POINTER : _to->GetProxy(destQueue, cid, aOuter, iid, proxyType, result); } 


#include "nsProxyEvent.h"

#define NS_XPCOMPROXY_CONTRACTID "@mozilla.org/xpcomproxy;1"
#define NS_XPCOMPROXY_CLASSNAME "XPCom Proxy"

#define NS_PROXYEVENT_MANAGER_CID                \
{ 0xeea90d41, 									 \
  0xb059, 										 \
  0x11d2,						                 \
 {0x91, 0x5e, 0xc1, 0x2b, 0x69, 0x6c, 0x93, 0x33}\
} 

/**
 * Helper function for code that already has a link-time dependency on
 * libxpcom and needs to get proxies in a bunch of different places.
 * This way, the caller isn't forced to get the proxy object manager
 * themselves every single time, thus making the calling code more
 * readable.
 */
extern NS_COM nsresult
NS_GetProxyForObject(nsIEventQueue *destQueue, 
                     REFNSIID aIID, 
                     nsISupports* aObj, 
                     PRInt32 proxyType, 
                     void** aProxyObject);

#endif /* __gen_nsIProxyObjectManager_h__ */
