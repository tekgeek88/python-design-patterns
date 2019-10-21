from ObserverDesignPattern.NewsPublisherExample.news_publisher import NewsPublisher
from ObserverDesignPattern.NewsPublisherExample.subscribers import SMSSubscriber, EmailSubscriber, AnyOtherSubscriber


########################################################
#                   Main Program
########################################################
if __name__ == '__main__':
    news_publisher = NewsPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)

    print(f"Subscribers: {news_publisher.subscibers()}")
    print()

    news_publisher.addNews("Hello World!")
    news_publisher.notifySubscribers()

    print()
    print(f"Detached: {type(news_publisher.detach()).__name__}")

    print()
    print(f"Subscribers: {news_publisher.subscibers()}")

    news_publisher.addNews("My second news!")
    news_publisher.notifySubscribers()