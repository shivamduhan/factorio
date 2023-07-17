

script.on_event({defines.events.on_tick},

   function (e)
	  --player.print(1234*5678)
      if e.tick % 60 == 0 then --common trick to reduce how often this runs, we don't want it running every tick, just 1/second

        for _, player in pairs(game.players) do

          if (player.character ~= nil) and player.connected and player.valid and player.character.valid then

            player.gui.top.greeting.caption = "Hello there!"
            player.gui.top["greeting"].caption = "\n".."\n".."\n".."        "..player.position.x .. ", " .. player.position.y.."        ".."\n".."\n".."\n"

                 --player.print(1234*5678)
                 --player.print("Its working")
  		      local ele = 0
  		      local entity="belt"
  		      local surface=player.surface
  	        local count=0

  		      for key, ent in pairs(surface.find_entities_filtered({force=player.force})) do
    			    if string.find(ent.name,entity) then
    		          count=count+1
    				 -- ele = player.get_power_usage(entity)

    			    end

            end
              player.print("Number of belts: " .. count)

		      end

        end

      end

   end

)



script.on_event({defines.events.on_player_created},

   function()
	  for _, player in pairs(game.players) do

		if (player.character ~= nil) and player.connected and player.valid and player.character.valid then
          player.gui.top.add{type="text-box", name="greeting", caption="Hi"}


           player.surface.always_day = true

           player.surface.peaceful_mode = true

           player.force.research_all_technologies()

		   player.force.recipes["pistol"].enabled=false
		   --player.force.technologies['military'].researched=false;
		   player.force.recipes["firearm-magazine"].enabled=false
           player.force.recipes["light-armor"].enabled=false
		   player.force.recipes["radar"].enabled=false
		   --player.force.recipes["stone-wall"].enabled=true


		end

	  end

   end

)
