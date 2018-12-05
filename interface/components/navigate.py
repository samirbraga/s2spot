class Navigate(object):
    listeners = { '__all__': [] }
    pages = []
    current_page = None
    current_data = None
    app = None

    @classmethod
    def setContainer(self, container):
        Navigate.container = container

    @classmethod
    def addPage(self, actived, key, kind, component, label,):
        Navigate.pages.append({ 'key': key, 'actived': actived, 'kind': kind, 'component': component, 'label': label })

    @classmethod
    def setApp(self, app):
        Navigate.app = app

    @classmethod
    def goto(self, page_key, current_data=None):
        for i, page in enumerate(Navigate.pages):
            if page['actived']:
                page['component'].unpack()

            Navigate.pages[i]['actived'] = False

            if page['key'] == page_key:
                if current_data == None:
                    Navigate.current_data = None
                else:
                    Navigate.current_data = current_data

                Navigate.pages[i]['actived'] = True
                Navigate.current_page = Navigate.pages[i]
                page['component'].pack()

                for cb in Navigate.listeners['__all__']:
                    cb(Navigate.pages[i])

                if page_key in Navigate.listeners:
                    for cb in Navigate.listeners[page_key]:
                        cb(Navigate.pages[i])

    @classmethod
    def addListener(self, page_key, callback):
        if page_key != '__all__':
            if page_key in Navigate.listeners:
                Navigate.listeners[page_key].append(callback)
            else:
                Navigate.listeners[page_key] = [callback]
        else:
            Navigate.listeners[page_key].append(callback)