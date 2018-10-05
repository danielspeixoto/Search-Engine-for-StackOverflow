
def filter(event)
    array = Array.new

    event.get('relations').each { |kvpair|
        array.push kvpair['value']['related_post_id']
    }

    event.set("relations", array)
    return [event]
end