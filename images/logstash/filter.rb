def filter(event)
    array = Array.new

    event.get('relations').each { |item|
        array.push item["post"]
    }

    event.set("relations", array)
    return [event]
end

test "post relations" do

  in_event { { "relations" => [{"post" => 1}, {"post" => 3}] } }

  expect("transform object to int array") do |events|
    events[0].get('relations') == [1, 3]
  end
end