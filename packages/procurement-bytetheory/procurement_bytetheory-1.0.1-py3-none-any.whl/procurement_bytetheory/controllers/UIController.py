from procurement_bytetheory.controllers.Observer import Observer
from procurement_bytetheory.model.Business import Business


class UIController(Observer):
    def __init__(self):
        super().__init__()
        self.view = None
        self.business = None

    def setView(self, view):
        self.view = view

    def setBusiness(self, business):
        self.business = business

    def update(self, message="", payload={}):
        self.view.update(message, payload)

    def createBusiness(self, name, moneyAmount):
        newBusiness = Business(name, moneyAmount)
        newBusiness.attachObserver(self)
        newBusiness.save()
        newBusiness.notifyObservers("Business created", newBusiness)
        self.setBusiness(newBusiness)

    def seedMarket(self):
        self.business.market.seedMarket()
        self.business.market.save()

    def buyCheapest(self, itemName=None):
        self.business.buyCheapest(itemName)
        self.business.save()
        self.business.notifyObservers("Cheapest item bought", self.business)

    def buyAsManyAsPossible(self, itemName=None):
        self.business.buyAsManyAsPossible(itemName)
        self.business.save()
        self.business.notifyObservers("Bought as many as possible", self.business)

    def sellItem(self, itemName=None):
        self.business.sellItem(itemName)
        self.business.save()
        self.business.notifyObservers("Sold item", self.business)

    def liquidateInventory(self):
        self.business.liquidateInventory()
        self.business.save()
        self.business.notifyObservers("Liquidated inventory", self.business)
    
    def getNetWorth(self):
        return self.business.getNetWorth()
