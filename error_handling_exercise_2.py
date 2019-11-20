def add_to_list_in_dict(thedict, listname, element):
    try:
        if listname in thedict:
            l = thedict[listname]
            print("%s already has %d elements." % (listname, len(l)))
        else:
            thedict[listname] = []
            print("Created %s." % listname)

    except KeyError:
        print("your list doesn't exist yet")
    else:
        thedict[listname].append(element)
    finally:
        print("Thanks")

    print("Added %s to %s." % (element, listname))
    