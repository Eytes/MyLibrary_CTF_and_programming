<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use \App\Models\Item;
use Illuminate\Support\Carbon;
use File;

class EquipSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $json = File::get("database/data/tasks.json");
        $tasks = json_decode($json);

        foreach ($tasks as $item) {
            $completed_at = $item->completed == 1 ? Carbon::now()->format('Y-m-d H:i:s') : NULL;
            Item::create([
                "name" => $item->name,
                "completed" => $item->completed,
                "completed_at" => $completed_at,
                "created_at" => Carbon::now()->format('Y-m-d H:i:s'),
                "updated_at" => Carbon::now()->format('Y-m-d H:i:s'),
            ]);
        }
    }
}
